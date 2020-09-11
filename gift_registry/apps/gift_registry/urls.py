from django.urls import path

from gift_registry import views

app_name = 'gift_registry'

urlpatterns = [
    path(r'^add.*$', views.add_gift_to_registry, name="add_gift_to_registry"),
    path(r'^delete.*$', views.delete_gift_from_registry, name="delete_gift_from_registry"),
    #path(r'^purchace.*$'),
]
