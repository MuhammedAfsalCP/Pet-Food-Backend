from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from cart.models import Cart,CartItem
from orders.models import Order,OrderItem
import razorpay
from rest_framework import status
from decouple import config

# Create your views here.

class Checkout(APIView):
    
    def post(self,request):

        cartitem=CartItem.objects.filter(cart__user=request.user)
        cart=Cart.objects.filter(user=request.user)
        total_price=0
        address = request.data.get('address')
        if not address:
            return Response({"error": "Address is required"}, status=400)
        for item in cartitem:
            total_price=total_price+item.product.Price*item.quantity

        order_currency='INR'
        client=razorpay.Client(auth=(config('Razerpay_KeyId'),config('Razerpay_KeySecret')))
        total_price=int(total_price*100 )
        payment=client.order.create({'amount':total_price,'currency':'INR','payment_capture':1})
        
        order=Order.objects.create(user=request.user,order_id=payment['id'],address=address,total_price=total_price / 100)
        for item in cartitem:
            product=item.product
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item.quantity
                
            )
            product.Stock=product.Stock-item.quantity
            product.save()
            
        cart.delete()
        cartitem.delete()
        return Response("succesfully orderd",status=status.HTTP_202_ACCEPTED)

        