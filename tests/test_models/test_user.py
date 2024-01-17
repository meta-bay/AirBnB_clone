#!/usr/bin/python3
"""
test_user module
"""
from unittest import TestCase
import pycodestyle
from models.user import User


class TestUser(TestCase):
    """
    TestUser class
    """

    def test_pep(self):
        """Test PEP 8 compliance"""
        style_checker = pycodestyle.StyleGuide(quiet=True)
        result = style_checker.check_files(
            ['models/user.py', 'tests/test_models/test_user.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_class_doc(self):
        """Test class documentation"""
        class_doc = User.__doc__
        self.assertGreater(len(class_doc), 1)
