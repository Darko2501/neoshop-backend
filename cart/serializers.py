from rest_framework import serializers
from .models import Cart, CartItems
from products.models import Product
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']
class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
      

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'user','total_amount']

class CartItemSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True)
    class Meta:
        model = CartItems
        fields = ['id', 'cart', 'products']



