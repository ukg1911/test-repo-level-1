import unittest
from src.utils import calculate_area
from src.validator import validate_age, process_id

class TestProject1(unittest.TestCase):
    def test_area(self):
        self.assertEqual(calculate_area(2), 12.56)

    def test_validation(self):
        self.assertTrue(validate_age(25))

    def test_id(self):
        self.assertEqual(process_id(123), "123") # Will trigger the Type Error