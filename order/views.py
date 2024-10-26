from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from cart.models import Cart
from .serializers import OrderSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    try:
        cart = Cart.objects.get(user=request.user)  
        if not cart.cartitems.exists():  
            return Response({"message": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)
        
    
        order = Order.objects.create(user=request.user, cart=cart)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Cart.DoesNotExist:
        return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)


