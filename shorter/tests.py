from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.urls import resolve

from .models import Url
from .views import HomeView


class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomeView)

    def test_redirect_to_login_status_code(self):
        url = reverse('created_urls')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class NewUrlTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='guest', password='123')
        self.client.login(username='guest', password='123')

    def test_new_url_validate_data(self):
        url = reverse('home')
        data = {
            'url': 'https://abc.go.com/'
        }
        response = self.client.post(url, data)
        self.assertTrue(Url.objects.exists())
