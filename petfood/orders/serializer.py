from rest_framework import serializers
from .models import OrderItem,Order
from products.serializer import ProductsSeriealizer


class OrderItemSerializer(serializers.ModelSerializer):
    product=ProductsSeriealizer()

    class Meta:
        model=OrderItem
        fields=('product','quantity','status','item_subtotal')

class OrderSerializer(serializers.ModelSerializer):
    orderitems = OrderItemSerializer(many=True, source='items')

    
    class Meta:
        model=Order
        fields=('order_id','created_at','orderitems','address','total_price')

