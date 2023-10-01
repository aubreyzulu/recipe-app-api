"""Tests for the django admin modifications"""

from django.test import (Client, TestCase)
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test for django admin"""

    def setUp(self):
        email = 'admin@example.com'
        password = '123456656'
        self.client = Client()

        """1. Creation of admin user"""
        self.admin_user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.client.force_login(self.admin_user)

        """2. User creation"""
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="122334rre",
            name='test'
        )

    def test_users_list(self):
        """Test that users are listed on the page."""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page works"""
        url = reverse(
            'admin:core_user_change',
            args=[self.user.id]
        )
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
