#!/usr/bin/python3
'''Defines test cases for console'''

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage


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
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            instance_id = f.getvalue().strip()
            
            with patch('sys.stdout', new=StringIO()) as f_all:
                self.console.onecmd("all")
                output = f_all.getvalue().strip()
                self.assertIn(instance_id, output)

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

class TestHBNBCommandCountMethods(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        storage._FileStorage__objects = {}

    def test_base_model_count_method(self):
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("create BaseModel")
            
            with patch('sys.stdout', new=StringIO()) as f_count:
                self.console.onecmd("BaseModel.count()")
                output = f_count.getvalue().strip()
                self.assertNotEqual(output, "1")  # Assuming one instance was created

    def test_review_count_method(self):
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("create Review")
        
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("Review.count()")
            output = f_count.getvalue().strip()
            self.assertNotEqual(output, "1")

    def test_user_count_method(self):
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("create User")
        
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("User.count()")
            output = f_count.getvalue().strip()
            self.assertNotEqual(output, "1")

    def test_state_count_method(self):
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("create State")
        
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("State.count()")
            output = f_count.getvalue().strip()
            self.assertNotEqual(output, "1")

    def test_city_count_method(self):
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("create City")
        
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("City.count()")
            output = f_count.getvalue().strip()
            self.assertNotEqual(output, "1")

    def test_amenity_count_method(self):
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("create Amenity")
        
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("Amenity.count()")
            output = f_count.getvalue().strip()
            self.assertNotEqual(output, "1")  # Assuming one instance was created
    
    def test_place_count_method(self):
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("create Place")
        
        with patch('sys.stdout', new=StringIO()) as f_count:
            self.console.onecmd("Place.count()")
            output = f_count.getvalue().strip()
            self.assertNotEqual(output, "1")

class TestHBNBCommandShowMethods(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_base_model_show_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.show('id')")
            output = f.getvalue().strip()
            self.assertIn("BaseModel", output)
            self.assertIn("id", output)

    def test_review_show_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Review.show('id')")
            output = f.getvalue().strip()
            self.assertIn("Review", output)
            self.assertIn("id", output)

    def test_user_show_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.show('id')")
            output = f.getvalue().strip()
            self.assertIn("User", output)
            self.assertIn("id", output)

    def test_state_show_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.show('id')")
            output = f.getvalue().strip()
            self.assertIn("State", output)
            self.assertIn("id", output)

    def test_city_show_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.show('id')")
            output = f.getvalue().strip()
            self.assertIn("City", output)
            self.assertIn("id", output)

    def test_amenity_show_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Amenity.show('id')")
            output = f.getvalue().strip()
            self.assertIn("Amenity", output)
            self.assertIn("id", output)

    def test_place_show_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place.show('id')")
            output = f.getvalue().strip()
            self.assertIn("Place", output)
            self.assertIn("id", output)

    def test_show_command_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.show()")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)


if __name__ == '__main__':
    unittest.main()