from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.login_url = reverse('login') 

    def test_valid_login(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('inicio')) 