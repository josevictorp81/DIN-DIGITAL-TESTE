from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from core.models import Product
from core.serializes import ProductSerializer

USER_URL = reverse('signup')
TOKEN_URL = reverse('token')
CREATE_PRODUCT_URL = reverse('create-product')
LIST_PRODUCT_URL = reverse('list-product')


def detail_product_view(product_id):
    return reverse('list-product-id', args=[product_id])


class UserTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_user_success(self):
        payload = {'username': 'testuser', 'password': 'passwordtest'}

        res = self.client.post(USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    def test_create_user_failid(self):
        User.objects.create_user(username='testuser', password='passwordtest')
        payload = {'username': 'testuser', 'password': 'passwordtest'}

        res = self.client.post(USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_token_success(self):
        User.objects.create_user(username='testuser', password='passwordtest')
        payload = {'username': 'testuser', 'password': 'passwordtest'}

        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('access', res.data)
    
    def test_create_token_invalid(self):
        User.objects.create_user(username='testuser', password='passwordtest')
        payload = {'username': 'testuser', 'password': 'passwordtest1'}

        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', res.data)
    
    def test_create_token_no_user(self):
        payload = {'username': 'testuser', 'password': 'passwordtest1'}

        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', res.data)


class ProductPublicTest(APITestCase):
    def test_login_required(self):
        self.cliente = APIClient()

        res = self.client.get(CREATE_PRODUCT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class ProductPrivateTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='passwordtest')
        self.client.force_authenticate(user=self.user)
    
    def test_create_product(self):
        payload = {'name': 'testproduct', 'price': 2.5, 'quantity': 3}

        res = self.client.post(CREATE_PRODUCT_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_list_product(self):
        Product.objects.create(name='testproduct1', price=2.5, quantity=3)
        Product.objects.create(name='testproduct2', price=2.9, quantity=5)

        res = self.client.get(LIST_PRODUCT_URL)

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    
    def test_list_id_product(self):
        product = Product.objects.create(name='testproduct1', price=2.5, quantity=3)
        Product.objects.create(name='testproduct2', price=2.9, quantity=5)

        url = detail_product_view(product.id)
        res = self.client.get(url)
        serializer = ProductSerializer(product)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
