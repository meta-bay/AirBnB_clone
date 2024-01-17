#!/usr/bin/python3
"""
test_city module
"""
from unittest import TestCase
import pycodestyle
from models.city import City


class TestCity(TestCase):
    """
    TestCity class
    """

    def test_pep(self):
        """Test PEP 8 compliance"""
        style_checker = pycodestyle.StyleGuide(quiet=True)
        files_to_check = ['models/city.py', 'tests/test_models/test_city.py']
        result = style_checker.check_files(files_to_check)
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_class_doc(self):
        """Test class documentation"""
        class_doc = City.__doc__
        self.assertGreater(len(class_doc), 1)
