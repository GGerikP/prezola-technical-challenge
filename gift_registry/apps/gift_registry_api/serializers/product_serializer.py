
from rest_framework import serializers

from gift_registry_api.model_lib.product import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
              'id'
            , 'name'
            , 'brand'
            , 'price'
            , 'currency'
            , 'in_stock_quantity'
        )

