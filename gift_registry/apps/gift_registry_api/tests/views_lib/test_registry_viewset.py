import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from unittest.mock import patch, MagicMock

from gift_registry_api.models import Registry
from gift_registry_api.models import Gift
from gift_registry_api.models import Product
from gift_registry_api.views_lib.registry_viewset import RegistryViewSet

class RegistryViewSetTestCase(TestCase):

    def get_registry_json(self):
        reg_json = json.dumps({
              'id':1
            , 'registry_owner':1
            , 'description':'registry 1'
            , 'gifts':[
                {
                  'id':1
                , 'purchase_status':'AVAILABLE'
                , 'product':{
                      'id':1
                    , 'name':'name 1'
                    , 'brand':'brand'
                    , 'price':'1.00'
                    , 'currency':'GBP'
                    , 'in_stock_quantity':1
                    }
                },{
                  'id':2
                , 'purchase_status':'PURCHASED'
                , 'product':{
                      'id':2
                    , 'name':'name 2'
                    , 'brand':'brand'
                    , 'price':'1.00'
                    , 'currency':'GBP'
                    , 'in_stock_quantity':1
                }
            }]
        })
        return reg_json

    def setUp(self):
        self.pk = 1
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.registry = Registry.objects.create(registry_owner=self.user, description="registry 1")
        self.product_1 = Product.objects.create(name="name 1", brand="brand", price=1.00, currency="GBP", in_stock_quantity=1)
        self.product_2 = Product.objects.create(name="name 2", brand="brand", price=1.00, currency="GBP", in_stock_quantity=1)
        Gift.objects.create(registry=self.registry, product=self.product_1)
        Gift.objects.create(registry=self.registry, product=self.product_2, purchase_status="PURCHASED")

    def test_retrieve_registry_success(self):
        """Test the string representation of Registries"""

        api_request = APIRequestFactory().get("/registry/1")
        detail_view = RegistryViewSet.as_view({'get': 'retrieve'})
        response = detail_view(api_request, pk=self.pk)

        self.assertEqual(response.status_code, 200)
        json_resp = json.dumps(response.data)
        self.assertEqual(json_resp, self.get_registry_json())


