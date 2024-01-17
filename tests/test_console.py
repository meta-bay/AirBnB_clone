#!/usr/bin/python3
''' test the console '''
import console
import json
import os
import sys
from unittest import TestCase
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBConsole(TestCase):
    ''' The HBNB console test class '''

    def test_docstrings(self):
        ''' tests the docstrings '''
        self.assertTrue(len(console.__doc__) >= 1)

    def test_the_prompt(self):
        ''' tests the prompt '''
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        ''' tests the emptyline '''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_quit(self):
        ''' tests quit '''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_the_EOF(self):
        ''' tests EOF '''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
