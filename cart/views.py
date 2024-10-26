from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItems
from products.models import Product
from .serializers import CartSerializer, CartItemSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_or_create_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return Response(CartSerializer(cart).data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def clear_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitems.all()
    
    for item in cart_items:
        product = item.products
        product.stock += 1  
        product.save()
    
    cart_items.delete()  
    cart.delete()  
    
    return Response({"message": "Cart cleared and products returned to stock"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product_id = request.data.get('product_id')
    
    try:
        product = Product.objects.get(id=product_id)
        if product.stock <= 0:
            return Response({'error': 'Product is out of stock'}, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    
    cart_item = CartItems.objects.create(cart=cart, products=product)
    product.stock -= 1  
    product.save()

    return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_cart_item(request, pk):
    try:
        cart_item = CartItems.objects.get(id=pk)
        product = cart_item.products
        product.stock += 1  
        product.save()
        cart_item.delete()
        
        return Response({"message": "Cart item deleted and product stock restored"}, status=status.HTTP_204_NO_CONTENT)
    except CartItems.DoesNotExist:
        return Response({"message": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_cart_items(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitems.all()
    return Response(CartItemSerializer(cart_items, many=True).data)

