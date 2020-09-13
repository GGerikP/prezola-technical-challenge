from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from gift_registry_api.model_lib.product import Product
from gift_registry_api.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    Product `list`, `create`, `retrieve`, `update`, and `destroy` actions
    '''
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all()

