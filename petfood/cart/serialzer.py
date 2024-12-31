from rest_framework import serializers
from .models import Cart,CartItem


class CartItemSerializer(serializers.ModelSerializer):
    

    class Meta:
        model=CartItem
        fields=('product','quantity','item_subtotal')

class CartSerializer(serializers.ModelSerializer):
    cartitems=CartItemSerializer(many=True)
    total_price=serializers.SerializerMethodField(method_name='total')

    def total(self,obj):
        cart_Items=obj.cartitems.all()
        return sum(Item.item_subtotal for Item in cart_Items)
    class Meta:
        model=Cart
        fields=('user','cartitems','total_price')