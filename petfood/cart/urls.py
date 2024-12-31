
from django.urls import path
from .views import CartView
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('cartdetails',CartView)




urlpatterns = [
    
    
]+router.urls
