
from django.urls import path,include
from .views import ProductDetails,ProductCategory
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('productdetails',ProductDetails)


urlpatterns = [
      path('productcatogory/<str:ctg>/',ProductCategory.as_view())
]+router.urls

