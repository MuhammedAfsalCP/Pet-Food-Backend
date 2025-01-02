
from django.urls import path,include
from .views import ProductDetails
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('productdetails',ProductDetails)


urlpatterns = [
      
]+router.urls

