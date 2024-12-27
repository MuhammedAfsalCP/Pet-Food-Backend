from django.shortcuts import render
from .serializer import ProductsSeriealizer
from rest_framework.viewsets import ModelViewSet
from .models import User,Products
# Create your views here.

# class UserDetails(ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserRegisterSerializer



class ProductDetails(ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductsSeriealizer