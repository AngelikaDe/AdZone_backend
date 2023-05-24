from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from ads.models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
import json

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['post','get', 'delete']


    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data['id'], status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        fields = None
        try:
            data = json.loads(request.body)
            fields = data.get('fields')
        except json.JSONDecodeError:
            pass

        response_data = {
            'name': product.name,
            'price': product.price,
            'main_photo': product.photo_link1 if product.photo_link1 else None,
        }
        if fields and 'description' in fields:
            response_data['description'] = product.description
            
        if fields and 'all_photos' in fields:
            response_data['all_photos'] = product.photo_link2 if product.photo_link2 else None, product.photo_link3 if product.photo_link3 else None
        return Response(response_data)


