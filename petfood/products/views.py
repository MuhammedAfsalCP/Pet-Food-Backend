from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ProductsSeriealizer
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from .models import Products
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.views import APIView

# Create your views here.

class ProductPagination(PageNumberPagination):
    page_size = 5 
    page_size_query_param = 'page_size'  
    max_page_size = 100  
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class ProductDetails(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSeriealizer
    pagination_class = ProductPagination

    def get_permissions(self):
        

        if self.request.method in ['PUT', 'POST', 'DELETE', 'PATCH']:
            return [IsAdminUser()]  
        else:
            return [AllowAny()]  
        
