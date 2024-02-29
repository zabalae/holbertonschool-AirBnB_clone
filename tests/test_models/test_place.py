#!/usr/bin/python3
'''Creates test cases for Place Class'''

import unittest
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    '''Test cases for Place Class'''
    def test_place_instance(self):
        '''Checks if an instance of the "Place" class can be created'''
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_default_values(self):
        '''Verifies that the default values of various attributes
            are as expected
        '''
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_attribute_assignment(self):
        '''Tests the assignment of values to the attributes
            of the "Place" class
        '''
        place = Place()
        place.city_id = "12"
        place.user_id = "345"
        place.name = "Cozy Cabin"
        place.description = "Cozy cabin near lake"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 80
        place.latitude = 42.2728
        place.longitude = -72.0414
        place.amenity_ids = [1, 2, 3]

        self.assertEqual(place.city_id, "12")
        self.assertEqual(place.user_id, "345")
        self.assertEqual(place.name, "Cozy Cabin")
        self.assertEqual(place.description, "Cozy cabin near lake")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 80)
        self.assertEqual(place.latitude, 42.2728)
        self.assertEqual(place.longitude, -72.0414)
        self.assertEqual(place.amenity_ids, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
