#!/usr/bin/python3
'''Creates test cases for FileStorage'''

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage:
    '''Class with test cases for FileStorage'''

    def setUp(self):
        '''This method will be called before each test'''
        self.file_storage = FileStorage()

    def tearDown(self):
        '''This method will be called after each test'''
        pass

    def test_new_and_all(self):
        '''Tests if new() correctly adds an object to __objects
            and all() returns the expected dictionary
        '''
        obj1 = __objects(id=1, name='example1')
        obj2 = __objects(id=2, name='example2')

        self.file_storage.new(obj1)
        self.file_storage.new(obj2)
        self.file_storage.save()

        new_file_storage = FileStorage()
        new_file_storage.reload()

        self.assertEqual(new_file_storage.all(),
                {'__objects.1': obj1, '__objects.2': obj2})

    def test_save_empty(self):
        '''Tests if save() works correctly when __objects is empty'''
        self.file_storage.save()

    def test_reload_nonexistent_file(self):
        '''Tests if reload() handles the case where the JSON
            file doesn't exist
        '''
        self.file_storage.reload()

    def test_reload_corrupted_file(self):
        '''Tests if reload() handles the case where the JSON
            file is corrupted
        '''
        with open(self.file_storage._FileStorage__file_path,
                'w', encoding='UTF-8') as file:
            file.write("corrupted data")

        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {})

if __name__ == '__main__':
    unittest.main()
