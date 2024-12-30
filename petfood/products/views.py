from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ProductsSeriealizer

from .models import Products
# Create your views here.
class ProductDetails(ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductsSeriealizer

