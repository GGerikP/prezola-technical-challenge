
from django.db import models

from gift_registry_api.apps import GiftRegistryAPIConfig
from gift_registry_api.model_lib.registry import Registry
from gift_registry_api.model_lib.product import Product

class RegistryProduct(models.Model):

    # Primary Field: id is automatically created for us
    # but it'd be better to create it as a uuid field

    class Meta:
        app_label = GiftRegistryAPIConfig.name
        verbose_name = 'Registry Product'
        verbose_name_plural = 'Registry Products'
        unique_together = (('registry_id', 'product_id'),)

    registry_id: int = models.ForeignKey(
          Registry
        , on_delete=models.CASCADE
        , blank=False
        , null=False
    )

    product_id: int = models.ForeignKey(
          Product
        , on_delete=models.CASCADE
        , blank=False
        , null=False
    )

    def __str__(self):
        ret = "Registry Product: Registry ID={registry_id}, Product ID={product_id}".format(
              registry_id=self.registry_id
            , product_id=self.product_id
        )
        return ret

