#!/usr/bin/python3
'''Creates test cases for user'''

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUserClass(unittest.TestCase):
    '''Test cases for User Class'''

    def setUp(self):
        '''Creates instances of the User class for testing'''
        self.user1 = User(email="user1@example.com", password="pass123", first_name="John", last_name="Doe")
        self.user2 = User(email="user2@example.com", password="pass456", first_name="Jane", last_name="Smith")

    def test_attributes(self):
        '''Tests if the attributes are initialized correctly'''
        self.assertEqual(self.user1.email, "user1@example.com")
        self.assertEqual(self.user1.password, "pass123")
        self.assertEqual(self.user1.first_name, "John")
        self.assertEqual(self.user1.last_name, "Doe")

        self.assertEqual(self.user2.email, "user2@example.com")
        self.assertEqual(self.user2.password, "pass456")
        self.assertEqual(self.user2.first_name, "Jane")
        self.assertEqual(self.user2.last_name, "Smith")

    def test_inheritance(self):
        '''Tests if User class inherits from BaseModel'''
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_firstname(self):
        '''Test User first name'''
        u1 = User()
        u1.first_name = "Liz"
        self.assertEqual(self.u1.first_name, "Liz")

    def test_user_lastname(self):
        ''''Test User last name'''
        u1 = User()
        u1.last_name = "Zabala"
        self.assertEqual(self.u1.last_name, "Zabala")

    def test_user_email(self):
        '''Test User email'''
        u1 = User()
        u1.email = "Liz@example.com"
        self.assertEqual(self.u1.email, "Liz@example.com")

    # def test_string_representation(self):
    #     '''Tests the __str__ method to ensure it returns
    #         a meaningful string
    #     '''
    #     self.assertEqual(str(self.user1), "User(email='user1@example.com', password='pass123', "
    #                                        "first_name='John', last_name='Doe')")
    #     self.assertEqual(str(self.user2), "User(email='user2@example.com', password='pass456', "
    #                                        "first_name='Jane', last_name='Smith')")

if __name__ == '__main__':
    unittest.main()
