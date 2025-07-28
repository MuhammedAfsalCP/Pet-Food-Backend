from rest_framework import serializers

from products.serializer import ProductsSerializer

from .models import Order, OrderItem,Notification


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = OrderItem
        fields = ("product", "quantity", "status", "item_subtotal", "id")


class OrderSerializer(serializers.ModelSerializer):
    orderitems = OrderItemSerializer(many=True, source="items")

    class Meta:
        model = Order
        fields = ("order_id", "created_at", "orderitems", "address", "total_price","updated_at")


class AllOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("order_id", "created_at", "total_price", "id")

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'message', 'created_at', 'is_read']