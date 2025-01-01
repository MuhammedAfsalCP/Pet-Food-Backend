from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from cart.models import Cart,CartItem
from orders.models import Order,OrderItem
import razorpay

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
        client=razorpay.Client(auth=('rzp_test_JtEUXj0BHIAbcC','WP8YrUHU4U3BWEiFAlOyqTfL'))
        total_price=int(total_price )
        payment=client.order.create({'amount':total_price,'currency':'INR','payment_capture':1})
        
        order=Order.objects.create(user=request.user,order_id=payment['id'],address=address,total_price=total_price / 100)
        for item in cartitem:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
        
        return Response(address)

        