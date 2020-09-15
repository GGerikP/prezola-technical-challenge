from django.contrib import admin

from gift_registry_api.models import Product
from gift_registry_api.models import Registry

admin.site.register(Product)
admin.site.register(Registry)
