from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ProductsSeriealizer
from rest_framework.pagination import PageNumberPagination
from .models import Products
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.views import APIView

# Create your views here.

class ProductPagination(PageNumberPagination):
    page_size = 5  # Items per page
    page_size_query_param = 'page_size'  # Allows the client to specify page size
    max_page_size = 100  # Max items per page
class ProductDetails(ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductsSeriealizer
    pagination_class=ProductPagination
    def get_permissions(self):
        if self.request.method in ['PUT', 'POST', 'DELETE', 'PATCH']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()
