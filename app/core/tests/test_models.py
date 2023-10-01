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
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tests if new user emails is normalized"""
        sample_emails = [
            ["test1@EXample.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.com", "TEST3@example.com"],
            ["test4@example.Com", "test4@example.com"]
        ]
        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(email=email, password="1234ed")
            self.assertEqual(expected_email, user.email)
