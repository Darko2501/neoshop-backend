from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  
    cart = serializers.PrimaryKeyRelatedField(read_only=True)  

    class Meta:
        model = Order
        fields = ['id', 'user', 'cart', 'created_at', 'order_status', 'payment_status']
        read_only_fields = ['id', 'created_at', 'user', 'cart']