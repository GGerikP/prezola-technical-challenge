import json
import logging

logger = logging.getLogger(__name__)

from rest_framework import status, viewsets
from rest_framework import permissions

from gift_registry_api.models import Product
from gift_registry_api.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    Product `list`, `create`, `retrieve`, `update`, and `destroy` actions
    '''
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all()

