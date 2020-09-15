import json

from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework import permissions
from rest_framework.response import Response

from gift_registry_api.models import Product
from gift_registry_api.serializers.product_serializer import ProductSerializer

from gift_registry_api.models import Registry
from gift_registry_api.serializers.registry_serializer import RegistrySerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    Product `list`, `create`, `retrieve`, `update`, and `destroy` actions
    '''
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all()

class RegistryViewSet(viewsets.ModelViewSet):
    '''
    Product `list`, `create`, `retrieve`, `update`, and `destroy actions
    '''
    serializer_class = RegistrySerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Registry.objects.all()

    def partial_update(self, request, pk=None):
        #serialized = RegistrySerializer(request.user, data=request.data, partial=True)
        #serialized.is_valid()

        registry = Registry.objects.get(id=pk)

        print("registry = " + str(registry))

        data = json.loads(request.body)
        print("data = " + str(data))
        product = data["purchased_product"]
        print("product = " + str(product))

        registry.products.remove(Product.objects.get(id=product["id"]))

        print("Registry = " + str(registry))

        serialized = RegistrySerializer(request.user, data=registry, partial=True)
        serialized.is_valid()
        return Response(serialized)

