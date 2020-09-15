
from django.db import models
from uuid import uuid4
import decimal

from gift_registry_api.apps import GiftRegistryAPIConfig

class Registry(models.Model):

    # Primary Field: id is automatically created for us
    # but it'd be better to create it as a uuid field

    class Meta:
        app_label = GiftRegistryAPIConfig.name
        verbose_name = 'Registry'
        verbose_name_plural = 'Registrys'

    registry_owner = models.ForeignKey(
          'auth.User'
        , on_delete=models.CASCADE
        , blank=False
        , null=False
    )

    description = models.CharField(
          max_length=128
        , blank=False
        , null=False
    )

    products = models.ManyToManyField(
          'gift_registry_api.Product'
        , related_name='registries'
        , symmetrical=False
        , blank=True
    )

    def __str__(self):
        ret = "Registry: ID={id}, username={username} ({user_id}), description={description}".format(
              id=self.id
            , username=self.registry_owner.username
            , user_id=self.registry_owner.id
            , description=self.description
        )
        return ret

