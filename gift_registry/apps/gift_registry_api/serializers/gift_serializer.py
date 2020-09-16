
from rest_framework import serializers

from gift_registry_api.models import Gift
from gift_registry_api.serializers.product_serializer import ProductSerializer

class GiftSerializer(serializers.ModelSerializer):

    product = ProductSerializer(
          many=False
        , read_only=True
    )

    class Meta:
        model = Gift
        fields = (
              'id'
            , 'purchase_status'
            , 'product'
        )

