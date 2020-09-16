import json

from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework import permissions
from rest_framework.response import Response

from gift_registry_api.models import Product
from gift_registry_api.serializers.product_serializer import ProductSerializer

from gift_registry_api.models import Registry
from gift_registry_api.serializers.registry_serializer import RegistrySerializer

from gift_registry_api.models import Gift
from gift_registry_api.serializers.gift_serializer import GiftSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    Product `list`, `create`, `retrieve`, `update`, and `destroy` actions
    '''
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all()

class RegistryViewSet(viewsets.ModelViewSet):
    '''
    Registry `list`, `create`, `retrieve`, `update`, and `destroy` actions
    '''
    serializer_class = RegistrySerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Registry.objects.all()

    def retrieve(self, request, pk=None):

        purchase_status = request.query_params.get('purchase_status', None)
        #TODO: validate the purchase_status input

        if purchase_status is not None:
            gifts = Gift.objects.filter(purchase_status=purchase_status.upper())
            filtered_registry = Registry.objects \
                .prefetch_related(Prefetch('gifts', gifts)) \
                .get(pk=pk)

            serialized = RegistrySerializer(filtered_registry)
        else:
            registry = Registry.objects.get(pk=pk)
            serialized = RegistrySerializer(registry)

        print("Returning data: " + str(serialized.data))

        return Response(serialized.data)

    def partial_update(self, request, pk=None):
        registry = Registry.objects.filter(id=pk)
        data = json.loads(request.body)

        print("request.body" + str(data))

        gift = data["purchased_gift"]

        print("gift = " + str(gift))

        reg_gift = Gift.objects.get(id=gift["id"])
        reg_gift.purchase_status = 'PURCHASED'
        reg_gift.save()

        reg_product = Product.objects.get(id=gift["product"]["id"])
        reg_product.in_stock_quantity -= 1
        reg_product.save()

        return self.retrieve(request, pk)


class GiftViewSet(viewsets.ModelViewSet):
    '''
    Registry Product `list`, `create`, `retrieve`, `update`, and `destroy` actions
    '''
    serializer_class = GiftSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Gift.objects.all()


