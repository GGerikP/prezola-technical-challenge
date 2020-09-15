
from rest_framework import serializers

from gift_registry_api.models import Registry
from gift_registry_api.serializers.product_serializer import ProductSerializer

class RegistrySerializer(serializers.ModelSerializer):

    products = ProductSerializer(
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
            , 'products'
        )

