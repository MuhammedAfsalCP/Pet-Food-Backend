from rest_framework import serializers
from .models import OrderItem,Order
from products.serializer import ProductsSeriealizer


class OrderItemSerializer(serializers.ModelSerializer):
    product=ProductsSeriealizer()
    class Meta:
        model=OrderItem
        fields=('product','quantity')


class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True)
    total_price=serializers.SerializerMethodField(method_name='total')

    def total(self,obj):
        order_Items=obj.items.all()
        return sum(OrderItem.item_subtotal for OrderItem in order_Items)

    

    class Meta:
        model=Order
        fields=('user','created_at','status','items','total_price','address')

