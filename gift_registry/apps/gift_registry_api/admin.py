from django.contrib import admin

from gift_registry_api.models import Product
from gift_registry_api.models import Registry
from gift_registry_api.models import Gift

#admin.site.register(Product)
#admin.site.register(Registry)

class GiftProfileInline(admin.StackedInline):
    model=Gift
    extra=1

class RegistryAdmin(admin.ModelAdmin):
    model=Registry
    save_on_top=True
    list_display=('registry_owner', 'description')
    inlines=[
        GiftProfileInline
    ]

admin.site.register(Product)
admin.site.register(Registry, RegistryAdmin)
admin.site.register(Gift)


