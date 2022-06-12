from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

USER_URL = reverse('user-list')
TOKEN_URL = reverse('token')

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
