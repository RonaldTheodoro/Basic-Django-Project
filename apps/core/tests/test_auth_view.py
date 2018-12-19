from django.contrib.auth.models import User
from django.test import TestCase
from django.shortcuts import resolve_url


class TestHome(TestCase):

    def setUp(self):
        user_data = {'username': 'admin', 'password': 'asdf1234'}
        self.user = User.objects.create_user(**user_data)
        self.client.login(**user_data)
        self.response = self.client.get(resolve_url('core:sample'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'core/sample.html')
