from django.contrib import admin
from django.urls import path, include
from gift_registry_api import urls as api_urls
from gift_registry_web import urls as web_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gift_registry_api.urls')),
    path('', include('gift_registry_web.urls')),
]
