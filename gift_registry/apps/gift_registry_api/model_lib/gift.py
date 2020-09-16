
from django.db import models

from gift_registry_api.apps import GiftRegistryAPIConfig
from gift_registry_api.models import Registry
from gift_registry_api.models import Product

class Gift(models.Model):

    # Primary Field: id is automatically created for us
    # but it'd be better to create it as a uuid field

    class Meta:
        app_label = GiftRegistryAPIConfig.name
        verbose_name = 'Gift'
        verbose_name_plural = 'Gifts'
        unique_together = ('registry', 'product', )

    registry: int = models.ForeignKey(
          Registry
        , related_name="gifts"
        , related_query_name="gift"
        , on_delete=models.CASCADE
        , blank=False
        , null=False
    )

    product: int = models.ForeignKey(
          Product
        , on_delete=models.CASCADE
        , blank=False
        , null=False
    )

    # TODO: This should be either an ENUM or a foreign key to a ref table
    purchase_status: str = models.CharField(
          max_length=32
        , blank=False
        , null=False
        , default='AVAILABLE'
    )

    def __str__(self):
        ret = "Registry Product: Registry ID={registry_id}, Product ID={product_id}, Purchase Status={purchase_status}".format(
              registry_id=self.registry.id
            , product_id=self.product.id
            , purchase_status=self.purchase_status
        )
        return ret

