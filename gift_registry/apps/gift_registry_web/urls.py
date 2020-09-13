
from django.urls import path, include
from gift_registry_web import views as web_views

app_name = 'gift_registry_web'

urlpatterns = [
    path('', web_views.show_web_index),
]
