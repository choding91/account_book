from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User


class UserTest(APITestCase):
    def test_signup(self):
        response = self.client.post(
            path=reverse("signup_view"),
            data={"email": "email@email.com", "password": "1234"},
        )
        self.assertEqual(response.status_code, 201)
