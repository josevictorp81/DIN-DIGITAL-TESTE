from rest_framework.test import APITestCase, APIClient

from core.models import Product

class ModelTest(APITestCase):
    def test_product_str(self):
        product = Product.objects.create(name='testproduct1', price=2.5, quantity=3)

        self.assertEqual(product.__str__(), product.name)
        