#!/usr/bin/python3
"""
test_amenity module
"""
from unittest import TestCase
import pycodestyle
from models.amenity import Amenity


class TestAmenity(TestCase):
    """
    TestAmenity class
    """

    def test_pep(self):
        """Test PEP 8 compliance"""
        style_checker = pycodestyle.StyleGuide(quiet=True)
        result = style_checker.check_files(
            ['models/amenity.py', 'tests/test_models/test_amenity.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_class_doc(self):
        """Test class documentation"""
        class_doc = Amenity.__doc__
        self.assertGreater(len(class_doc), 1)
