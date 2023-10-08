"""Tests for the user API"""

from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')

TOKEN_URL = reverse('user:token')


def create_user(**params):
    """Creates and returns a new user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the public feature of the user API"""

    def setUp(self):
        self.client = APIClient()

    def test_creating_user_success(self):
        """Test if creating a user is successful"""
        payload = {
            'email': 'test@example.com',
            'password': 'test1234',
            'name': 'test name'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_error(self):
        """Test if user with email exists"""

        payload = {
            'email': 'test@example.com',
            'password': 'test1234',
            'name': 'test name'
        }

        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Tests if password is less than 5 characters"""
        payload = {
            'email': 'test@example.com',
            'password': '123',
            'name': 'test name'
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exits = get_user_model().objects.filter(
            email=payload['email']).exists()

        self.assertFalse(user_exits)

    def test_create_token_for_user(self):
        """Test generate token for valid credentials"""
        user_payload = {
            'email': 'test@example.com',
            'password': '123345q',
            'name': 'test name'
        }
        create_user(**user_payload)

        login_payload = {
            "email": user_payload['email'],
            "password": user_payload['password']
        }
        res = self.client.post(TOKEN_URL, login_payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_bad_credentials(self):
        """Test returns error is credentials are invalid"""
        user_payload = {
            'email': 'test@example.com',
            'password': 'pass12345'
        }
        create_user(**user_payload)

        login_payload = {
            'email': user_payload['email'],
            'password': '343343dd'
        }
        res = self.client.post(TOKEN_URL, login_payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_blank_password(self):
        """Test login with blank password returns an error"""
        user_payload = {
            'email': 'test@example.com',
            'password': 'pass12345'
        }
        create_user(**user_payload)
        login_payload = {
            'email': user_payload['email'],
            'password': ''
        }
        res = self.client.post(TOKEN_URL, login_payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)