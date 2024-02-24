#!/usr/bin/python3
'''Creating test cases for BaseModel'''

import unittest
from base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_id_generation(self):
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.assertNotEqual(obj1.id, obj2.id)

    def test_str_method(self):
        obj = BaseModel()

        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save_method_updates_updated_at(self):
        obj = BaseModel()
        original_updated_at = obj.updated_at

        obj.save()

        self.assertNotEqual(original_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    __name__ == '__main__':
        unittest.main()
