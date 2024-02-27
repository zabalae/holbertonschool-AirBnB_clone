#!/usr/bin/python3
'''Creates test cases for Class State'''

import unittest
from models.state import State


class TestStateClass(unittest.TestCase):
    '''Test cases for Class State'''

    def test_state_instance(self):
        '''Checks if an instance of the "State" class can be created'''
        state = State()
        self.assertIsInstance(state, State)

    def test_state_name_default_value(self):
        '''Verifies that the default value of the "name" attribute
            is an empty string
        '''
        state = State()
        self.assertEqual(state.name, "")

    def test_state_name_assignment(self):
        '''Tests the assignment of a value to the "name" attribute'''
        state = State()
        state.name = "Florida"
        self.assertEqual(state.name, "Florida")

if __name__ == '__main__':
    unittest.main()
