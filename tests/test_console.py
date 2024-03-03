#!/usr/bin/python3
'''Creates test cases for console'''

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsoleCommands(unittest.TestCase):
    '''Test cases for the console's commands'''
    def setUp(self):
        self.console = HBNBCommand()

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('create BaseModel')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output != "")

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('show BaseModel 123')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('destroy BaseModel 123')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('all')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "[]")

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('update BaseModel 123 attribute value')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

if __name__ == '__main__':
    unittest.main()