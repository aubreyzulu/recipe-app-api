"""Test for models"""
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with a email successful"""
        email = 'test@exmple.com'
        password = "1233456dfg"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
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
            user = get_user_model().objects.create_user(
                email=email,
                password="1234ed"
            )
            self.assertEqual(expected_email, user.email)

    def test_new_user_without_email_raises_error(self):
        """Test creating a user without email raises an Error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="",
                password="123dggrr"
            )

    def test_creating_superuser(self):
        """Tests creating a superuser"""

        email = "admin@example.com"
        password = "12323dwdw"

        superuser = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_creating_recipe(self):
        """Test creating recipe is successful"""
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='e3rerefes'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='Spaghetti Carbonara',
            time_in_minutes=20,
            price=Decimal('10.99'),
            description="A classic Italian dish with creamy sauce, pancetta, and Parmesan"
        )

        self.assertEqual(str(recipe), recipe.title)
