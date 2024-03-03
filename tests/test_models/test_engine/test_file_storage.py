#!/usr/bin/python3
'''Creates test cases for FileStorage'''

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.place import Place


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

    def test_save_and_reload_non_empty_objects(self):
         '''Tests if save() and reload() work with non-empty objects'''
         original_instance = BaseModel()
         original_instance.save()

         instance_id = original_instance.id

         original_instance.new_key = 'new_value'
         original_instance.save()

         restored_instance = BaseModel(id=instance_id)

         storage.reload()

         loaded_instance = storage.all()[f"BaseModel.{instance_id}"]
         self.assertIn('new_key', loaded_instance.to_dict())
         self.assertEqual(loaded_instance.new_key, 'new_value')

    def testTypePath(self):
        self.assertEqual(type(storage.all()), dict)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_empty_reload(self):
        """ Empty reload function """
        obj = FileStorage()
        new_obj = BaseModel()
        obj.new(new_obj)
        obj.save()
        dict1 = obj.all()
        os.remove("file.json")
        obj.reload()
        dict2 = obj.all()
        self.assertTrue(dict2 == dict1)

    def test_reload(self):
        bm = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        storage.new(bm)
        storage.new(user)
        storage.new(state)
        storage.new(place)
        storage.new(city)
        storage.new(amenity)
        storage.new(review)
        storage.save()
        storage.reload()
        objs = FileStorage.__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + city.id, objs)
        self.assertIn("Amenity." + amenity.id, objs)
        self.assertIn("Review." + review.id, objs)

if __name__ == '__main__':
    unittest.main()
