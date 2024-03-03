#!/usr/bin/python3
'''Defines test cases for console'''

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsoleCommands(unittest.TestCase):
    '''Test cases for the console's commands'''
    def setUp(self):
        self.console = HBNBCommand()

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('quit')

    def test_EOF_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('EOF')

    def test_empty_line_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())

    def test_create_base_model_command(self):
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

    def test_base_model_update_with_dict_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update BaseModel 123 {'attribute_name': 'string_value'}")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

class TestHBNBCommandAllMethods(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_base_model_all_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.all()")
            output = f.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_review_all_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Review.all()")
            output = f.getvalue().strip()
            self.assertIn("Review", output)

    def test_user_all_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.all()")
            output = f.getvalue().strip()
            self.assertIn("User", output)

    def test_state_all_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.all()")
            output = f.getvalue().strip()
            self.assertIn("State", output)

    def test_city_all_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.all()")
            output = f.getvalue().strip()
            self.assertIn("City", output)

    def test_amenity_all_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Amenity.all()")
            output = f.getvalue().strip()
            self.assertIn("Amenity", output)

    def test_place_all_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place.all()")
            output = f.getvalue().strip()
            self.assertIn("Place", output)


if __name__ == '__main__':
    unittest.main()