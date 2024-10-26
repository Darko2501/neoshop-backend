from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .filters import ProductFilter

@api_view(['GET'])
@permission_classes([AllowAny])
def category_list(request):
    
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def product_list(request):
    filterset=ProductFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    
    serializer = ProductSerializer(filterset.qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def single_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
    
    serializer = ProductSerializer(product)
    return Response(serializer.data)

