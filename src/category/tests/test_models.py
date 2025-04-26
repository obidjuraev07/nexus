from django.test import TestCase
from ..models import Brand

class BrandTest(TestCase):
    def test_create_brand(self):
        brand = Brand.objects.create(name='Apple')
        self.assertEqual(brand.name, 'Apple')
