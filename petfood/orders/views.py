from django.shortcuts import render
from rest_framework.response import Response
from .serializer import OrderItemSerializer,OrderSerializer
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Order,OrderItem

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.db.models import Q
# Create your views here.
class ProductPagination(PageNumberPagination):
    page_size = 5  
    page_size_query_param = 'page_size'  
    max_page_size = 100  


class OrderView(ListAPIView):
    
    pagination_class=ProductPagination
    serializer_class=OrderSerializer
    def get_queryset(self):
        
        user = self.request.user
        return Order.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class OrderUpdate(APIView):
    def get(self,request,pk):
        try:
            product=OrderItem.objects.get(Q(id=pk)&~Q(status='Cancelled'))
            
        except:
              return Response("invalid Product",status=status.HTTP_400_BAD_REQUEST)
        
        serializer=OrderItemSerializer(product)
        return Response(serializer.data)

    def post(self,request,pk):
        try:
            product=OrderItem.objects.get(id=pk)
            try:
                statuz=request.data.get('status')
                product.status=statuz
                product.save()
                return Response('updated',status=status.HTTP_202_ACCEPTED)

            except:
                return Response("invalid Status",status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response("invalid Product",status=status.HTTP_400_BAD_REQUEST)
        

    
