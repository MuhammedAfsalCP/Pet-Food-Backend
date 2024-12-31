from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ProductsSeriealizer
from rest_framework.pagination import PageNumberPagination
from .models import Products
# Create your views here.

class ProductPagination(PageNumberPagination):
    page_size = 5  # Items per page
    page_size_query_param = 'page_size'  # Allows the client to specify page size
    max_page_size = 100  # Max items per page
class ProductDetails(ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductsSeriealizer
    pagination_class=ProductPagination

