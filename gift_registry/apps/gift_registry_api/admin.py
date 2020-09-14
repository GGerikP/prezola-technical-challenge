from django.contrib import admin

from gift_registry_api.models import Product
from gift_registry_api.models import Registry
from gift_registry_api.models import RegistryProduct

admin.site.register(Product)
admin.site.register(Registry)
admin.site.register(RegistryProduct)
