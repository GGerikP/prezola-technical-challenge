from django.contrib.auth.models import User
from django.test import TestCase
from unittest.mock import patch, MagicMock

from gift_registry_api.models import Registry
from gift_registry_api.models import Product
from gift_registry_api.models import Gift

class GiftTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.registry_1 = Registry.objects.create(registry_owner=self.user, description="registry 1")
        self.registry_2 = Registry.objects.create(registry_owner=self.user, description="registry 2")
        self.product_1 = Product.objects.create(name="prod1", brand="brand", price=1.00, currency='GBP', in_stock_quantity=1)
        self.product_2 = Product.objects.create(name="prod2", brand="brand", price=1.00, currency='GBP', in_stock_quantity=1)

    def test_gifts_can_share_products_success(self):
        """Test multiple gifts can have the same product"""
        Gift.objects.create(registry=self.registry_1, product=self.product_1)
        Gift.objects.create(registry=self.registry_2, product=self.product_1)
        assert True
