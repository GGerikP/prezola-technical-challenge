
from rest_framework import serializers

from gift_registry_api.models import Registry
from gift_registry_api.serializers.gift_serializer import GiftSerializer

class RegistrySerializer(serializers.ModelSerializer):

    gifts = GiftSerializer(
          many=True
        , read_only=False
    )

    class Meta:
        model = Registry
        partial = True
        fields = (
              'id'
            , 'registry_owner'
            , 'description'
            , 'gifts'
        )

