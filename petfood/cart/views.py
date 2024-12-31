from django.shortcuts import render
from .serialzer import CartItemSerializer,CartSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Cart,CartItem
# Create your views here.

class CartAdd(CreateAPIView,ListAPIView):
    serializer_class=CartItemSerializer
    permission_classes=[IsAuthenticated]
    def perform_create(self,serializer):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        serializer.save(cart=cart)
        
        return Response(cart)
    def get_queryset(self):
        # Get the cart items for the authenticated user
        user = self.request.user
        return CartItem.objects.filter(cart__user=user)

    def list(self, request, *args, **kwargs):
        # Override list method to return the cart items
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    

class CartDelete(APIView):
    def get(self,request,pk):
        try:
            cart_item=CartItem.objects.get(id=pk)
            serializer=CartItemSerializer(cart_item)
            return Response(serializer.data)
        except CartItem.DoesNotExist:
            return Response('cart not found',status=status.HTTP_404_NOT_FOUND)
        


    def delete(self,request,pk):
        try:
            cart_item=CartItem.objects.get(id=pk)
            cart_item.delete()
            return Response('item Deleted',status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

    
    
