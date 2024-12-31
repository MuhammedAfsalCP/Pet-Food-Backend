from django.shortcuts import render
from rest_framework.response import Response
from .serializer import OrderItemSerializer,OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import User
from .models import Order,OrderItem
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
# Create your views here.

# class Order_List(APIView):
#     def get(self,request,pk):
#         user =User.objects.get(id=pk)

#         orders = Order.objects.filter(user=user)
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class OrederCreate(CreateAPIView):
    serializer_class=OrderItemSerializer