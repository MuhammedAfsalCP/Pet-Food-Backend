from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductsSeriealizer,UserRegisterSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from .models import User,Products
# Create your views here.

class UserDetails(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializer




class ProductDetails(ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductsSeriealizer