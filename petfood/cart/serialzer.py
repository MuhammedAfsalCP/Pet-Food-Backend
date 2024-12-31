from rest_framework import serializers
from .models import Cart,CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=('product','quantity')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=('user',)