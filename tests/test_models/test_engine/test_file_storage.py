#!/usr/bin/python3
'''Creates test cases for FileStorage'''

import unittest
#from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from models import storage

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

#     def setUp(self):
#         '''This method will be called before each test'''
#         self.file_storage = FileStorage()

#     def tearDown(self):
#         '''This method will be called after each test'''
#         pass

#     def test_new_and_all(self):
#         '''Tests if new() correctly adds an object to __objects
#             and all() returns the expected dictionary
#         '''
#         obj1 = FileStorage.__objects(id=1, name='example1')
#         obj2 = FileStorage.__objects(id=2, name='example2')

#         self.file_storage.new(obj1)
#         self.file_storage.new(obj2)
#         self.file_storage.save()

#         new_file_storage = FileStorage()
#         new_file_storage.reload()

#         self.assertEqual(new_file_storage.all(),
#                 {'__objects.1': obj1, '__objects.2': obj2})

#     def test_save_empty(self):
#         '''Tests if save() works correctly when __objects is empty'''
#         self.file_storage.save()

#     def test_reload_nonexistent_file(self):
#         '''Tests if reload() handles the case where the JSON
#             file doesn't exist
#         '''
#         self.file_storage.reload()

#     def test_reload_corrupted_file(self):
#         '''Tests if reload() handles the case where the JSON
#             file is corrupted
#         '''
#         with open(self.file_storage._FileStorage__file_path,
#                 'w', encoding='UTF-8') as file:
#             file.write("corrupted data")

#         self.file_storage.reload()
#         self.assertEqual(self.file_storage.all(), {})

#     def test_reload(self):
#         new = BaseModel()
#         FileStorage.save()
#         FileStorage.reload()
#         for obj in FileStorage.all().values():
#             loaded = obj
#         self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

if __name__ == '__main__':
     unittest.main()
