from django.contrib.auth.models import User
from django.test import TestCase
from unittest.mock import patch, MagicMock

from gift_registry_api.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="product 1", brand="brand", price=1.00, currency="GBP", in_stock_quantity=1)

    def test_product_str_success(self):
        """Test the string representation of Registries"""
        prod_1 = Product.objects.get(pk=1)
        self.assertEqual(str(prod_1), 'Product: name=product 1, brand=brand, price=1.00, currency=GBP, in_stock_quantity=1')
