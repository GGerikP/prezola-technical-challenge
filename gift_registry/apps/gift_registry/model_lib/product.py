
from django.db import models
from uuid import uuid4
import decimal

class Product(models.Model):

    # Primary Field: id is automatically created for us
    # but it'd be better to create it as a uuid field

    name: str = models.CharField(
          max_length=128
        , unique=True
        , blank=False
        , null=False
    )

    brand: str = models.CharField(
          max_length=128
        , unique=True
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

