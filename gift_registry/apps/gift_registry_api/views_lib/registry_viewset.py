import json
import logging

logger = logging.getLogger(__name__)

from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework import permissions
from rest_framework.response import Response

from gift_registry_api.models import Product
from gift_registry_api.models import Registry
from gift_registry_api.serializers.registry_serializer import RegistrySerializer
from gift_registry_api.models import Gift

class RegistryViewSet(viewsets.ModelViewSet):
    '''
    Registry `list`, `create`, `retrieve`, `update`, and `destroy` actions
    '''
    serializer_class = RegistrySerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Registry.objects.all()

    def retrieve(self, request, pk=None):

        logger.info("Request received: request.data = {request_data}".format(request_data=str(request.data)))

        #TODO: validate the purchase_status input: should be an enum or ref table
        purchase_status = request.query_params.get('purchase_status', None)

        if purchase_status is not None:
            logger.info("Filtering gifts by purchase_status: {purchase_status}".format(purchase_status=purchase_status.upper()))
            gifts = Gift.objects.filter(purchase_status=purchase_status.upper())
            filtered_registry = Registry.objects \
                .prefetch_related(Prefetch('gifts', gifts)) \
                .get(pk=pk)

            serialized = RegistrySerializer(filtered_registry)
        else:
            registry = Registry.objects.get(pk=pk)
            serialized = RegistrySerializer(registry)

        logger.info("Returning data: serialized.data={serialized_data}".format(serialized_data=str(serialized.data)))

        return Response(serialized.data)

    def partial_update(self, request, pk=None):
        registry = Registry.objects.filter(id=pk)
        data = json.loads(request.body)

        logger.info("Request recieved: request.body={data}".format(data=str(data)))

        gift = data["purchased_gift"]

        reg_gift = Gift.objects.get(id=gift["id"])
        reg_gift.purchase_status = 'PURCHASED'
        logger.info("Updated gift: {gift}".format(gift=str(reg_gift)))
        reg_gift.save()

        reg_product = Product.objects.get(id=gift["product"]["id"])
        reg_product.in_stock_quantity -= 1
        logger.info("Updated product: {product}".format(product=str(reg_product)))
        reg_product.save()

        return self.retrieve(request, pk)

