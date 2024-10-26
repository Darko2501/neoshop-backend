from rest_framework import serializers
from .models import Category,Product
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model=Product
        fields = ['id', 'name', 'price', 'description','image']