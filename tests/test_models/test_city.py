#!/usr/bin/python3
'''Creates test cases for City Class'''

import unittest
from models.city import City


class TestCityClass(unittest.TestCase):
    '''Test cases for City Class'''
    def test_city_instance(self):
        '''Checks if an instance of the "City" class can be created'''
        city = City()
        self.assertIsInstance(city, City)

    def test_city_state_id_default_value(self):
        '''Verifies that the default value of the "state_id" attribute
            is an empty string
        '''
        city = City()
        self.assertEqual(city.state_id, "")

    def test_city_name_default_value(self):
        '''Verifies that the default value of the "name" attribute
            is an empty string
        '''
        city = City()
        self.assertEqual(city.name, "")

    def test_city_state_id_assignment(self):
        '''Tests the assignment of a value to the "state_id" attribute'''
        city = City()
        city.state_id = "FL"
        self.assertEqual(city.state_id, "FL")

    def test_city_name_assignment(self):
        '''Tests the assignment of a value to the "name" attribute'''
        city = City()
        city.name = "Orlando"
        self.assertEqual(city.name, "Orlando")

if __name__ == '__main__':
    unittest.main()
