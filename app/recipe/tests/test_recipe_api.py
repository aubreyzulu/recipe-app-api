"""Test for the recipe APIs"""
from django.test import TestCase
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe
from recipe.serializer import RecipeSerializer


def create_recipe(user, **params):
    """Create and return a sample recipe"""
    default_payload = {
        'title': 'Grilled Salmon',
        'price': 15.75,
        'time_in_minutes': 15,
        'description': 'Grilled salmon fillet with a side of lemon-butter sauce.',
        "link": "https://example.com/recipes/grilled-salmon"
    }

    default_payload.update(params)
    recipe = Recipe.objects.create(user=user, **default_payload)
    return recipe


class RecipeTests(TestCase):
    """"""
