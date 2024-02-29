#!/usr/bin/python3
'''Creates test cases for the Review Class'''

import unittest
from models.review import Review


class TestReviewClass(unittest.TestCase):
    '''Test cases for Review Class'''
    def test_review_instance(self):
        '''Checks if an instance of the "Review" class can be created'''
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_default_values(self):
        '''Verifies that the default values of various attributes
            are as expected
        '''
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attribute_assignment(self):
        '''Tests the assignment of values to the attributes
            of the "Review" class
        '''
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Beautiful place! Will visit again!"

        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Beautiful place! Will visit again!")

if __name__ == '__main__':
    unittest.main()
