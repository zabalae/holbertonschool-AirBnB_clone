#!/usr/bin/python3
'''Creating test cases for BaseModel'''

import unittest
from base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''Defines test cases for "BaseModel"'''
    def test_id_generation(self):
        '''Tests that each instance of BaseModel has a unique ID'''
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.assertNotEqual(obj1.id, obj2.id)

    def test_str_method(self):
        '''Tests the string representation of the BaseModel instance'''
        obj = BaseModel()

        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save_method_updates_updated_at(self):
        '''Tests that the save method updates the updated_at attribute'''
        obj = BaseModel()
        original_updated_at = obj.updated_at

        obj.save()

        self.assertNotEqual(original_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        '''Tests the to_dict method for serialization'''
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    __name__ == '__main__':
        unittest.main()
