#!/usr/bin/python3
'''Creates test cases for the Amenity Class'''

import unittest
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    '''Test cases for Amenity Class'''
    def test_amenity_instance(self):
        '''Checks if an instance of the "Amenity" class can be created'''
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_name_default_value(self):
        '''Verifies that the default value of the "name" attribute
            is an empty string
        '''
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_name_assignment(self):
        '''Tests the assignment of a value to the "name" attribute'''
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

if __name__ == '__main__':
    unittest.main()
