from django.contrib.auth.models import User
from django.test import TestCase
from unittest.mock import patch, MagicMock

from gift_registry_api.models import Registry

class RegistryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        Registry.objects.create(registry_owner=self.user, description="registry 1")
        Registry.objects.create(registry_owner=self.user, description="registry 2")

    def test_registry_str_success(self):
        """Test the string representation of Registries"""
        reg_1 = Registry.objects.get(pk=1)
        reg_2 = Registry.objects.get(pk=2)
        self.assertEqual(str(reg_1), 'Registry: ID=1, username=testuser (1), description=registry 1')
        self.assertEqual(reg_2.__str__(), 'Registry: ID=2, username=testuser (1), description=registry 2')
