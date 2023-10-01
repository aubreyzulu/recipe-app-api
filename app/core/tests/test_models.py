"""Test for models"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with a email successful"""
        email = 'test@exmple.com'
        password = "1233456dfg"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        print(user.email)
        self.assertTrue(user.check_password(password))
