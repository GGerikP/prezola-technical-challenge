
from django.urls import path, include
from gift_registry_web import views as web_views

app_name = 'gift_registry_web'

urlpatterns = [
    path('report', web_views.show_registry_gift_report),
    path('', web_views.show_web_index),
]
