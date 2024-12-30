
from django.urls import path
from .views import ProductDetails
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('admin/productdetails',ProductDetails)


urlpatterns = [
    
    
]+router.urls
