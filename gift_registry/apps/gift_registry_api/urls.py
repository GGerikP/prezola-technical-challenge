
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from gift_registry_api import views

app_name = 'gift_registry_api'

gift_registry_router = SimpleRouter(
    trailing_slash=True
)

gift_registry_router.register(
      'product'
    , views.ProductViewSet
    , basename=app_name + '-product'
)

gift_registry_router.register(
      'registry'
    , views.RegistryViewSet
    , basename=app_name + '-registry'
)

urlpatterns = [
    path('', include(gift_registry_router.urls)),
]
