#!/usr/bin/python3
'''Creates test cases for FileStorage'''

import unittest
#from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from models import storage


class SampleClass(unittest.TestCase):
    '''Sample Class for testing'''
    def __init__(self, id, name):
        self.id = id
        self.name = name

class TestFileStorage(unittest.TestCase):
    '''Class with test cases for FileStorage'''
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
    

    def testEmpty(self):
        original_instance = BaseModel()
        instance_dict = original_instance.to_dict()
        original_instance.save()
        restored_instance = BaseModel(**instance_dict)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def testReload(self):
        original_instance = BaseModel()
        storage.save()
        storage.reload()
        for loaded_instance in storage.all().values():
            loaded = loaded_instance
        self.assertEqual(original_instance.to_dict()['id'], loaded.to_dict()['id'])

    def test_save_empty(self):
        '''Tests if save() works correctly when __objects is empty'''
        storage.save()

    def test_reload_empty_file(self):
        '''Tests if reload() handles the case where
            the JSON file is empty
        '''
        storage.reload()

    def test_reload_non_existent_file(self):
        '''Tests if reload() handles the case where the JSON
            file doesn't exist
        '''
        file_path = storage._FileStorage__file_path
        storage._FileStorage__file_path = "non_existent_file.json"
        storage.reload()
        storage._FileStorage__file_path = file_path

    def test_save_and_reload_non_empty_objects(self):
         '''Tests if save() and reload() work with non-empty objects'''
         original_instance = BaseModel()
         instance_dict = original_instance.to_dict()
         original_instance.save()

         instance_dict['new_key'] = 'new_value'

         restored_instance = BaseModel(**instance_dict)
         self.assertNotEqual(os.path.getsize(storage._FileStorage__file_path), 0)

         storage.reload()
         loaded_instance = storage.all().values()
         self.assertEqual(loaded_instance.to_dict()['new_key'], 'new_value')

    def testTypePath(self):
        self.assertEqual(type(storage.all()), dict)

if __name__ == '__main__':
    unittest.main()
