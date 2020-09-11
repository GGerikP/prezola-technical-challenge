from django.contrib import admin
from django.urls import path
 gift_registry

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^', gift_registry.urls),
]
