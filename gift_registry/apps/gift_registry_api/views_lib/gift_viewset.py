import json
import logging

logger = logging.getLogger(__name__)

from rest_framework import status, viewsets
from rest_framework import permissions

from gift_registry_api.models import Gift
from gift_registry_api.serializers.gift_serializer import GiftSerializer

class GiftViewSet(viewsets.ModelViewSet):
    '''
    Registry Product `list`, `create`, `retrieve`, `update`, and `destroy` actions
    '''
    serializer_class = GiftSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Gift.objects.all()


