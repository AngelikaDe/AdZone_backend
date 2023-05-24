from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet


router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]