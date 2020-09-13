
from django.db import models
from uuid import uuid4
import decimal

from gift_registry_api.apps import GiftRegistryAPIConfig

class Product(models.Model):

    # Primary Field: id is automatically created for us
    # but it'd be better to create it as a uuid field

    class Meta:
        app_label = GiftRegistryAPIConfig.name
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        unique_together = (('name', 'brand'),)

    name: str = models.CharField(
          max_length=128
        , blank=False
        , null=False
    )

    brand: str = models.CharField(
          max_length=128
        , blank=False
        , null=False
    )

    price: decimal = models.DecimalField(
          max_digits=18
        , decimal_places=2
        , blank=False
        , null=False
        , default=0.0
    )

    # TODO: Convert this to an enum or a foreign key to an currency table
    currency: str = models.CharField(
          max_length=3
        , blank=False
        , null=False
    )

    in_stock_quantity: int = models.PositiveIntegerField(
          blank=False
        , null=False
        , default=0
    )

    def __str__(self):
        ret = "Product: name={name}, brand={brand}, price={price}, currency={currency}, in_stock_quantity={in_stock_quantity}".format(
              name=self.name
            , brand=self.brand
            , price=self.price
            , currency=self.currency
            , in_stock_quantity=self.in_stock_quantity
        )
        return ret

