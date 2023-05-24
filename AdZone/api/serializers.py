from rest_framework import serializers
from ads.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'photo_link1', 'price']
