from django.test import SimpleTestCase
from .calc import add, subtract


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        res = add(2, 2)
        self.assertEqual(res, 4)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = subtract(10, 5)
        self.assertEqual(res, 5)
