#!/usr/bin/python3
'''
Unit tests for Review Model
'''
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    '''
    Unit tests for Review Model.
    '''
    def test_review_inherits_from_base_model(self):
        '''
        Checks that the Review class Inherits from BaseModel
        '''
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_review_has_attributes(self):
        '''
        Checks that Review class has place_id, user_id and text attributes.
        '''
        new_review = Review()
        self.assertTrue('place_id' in new_review.__dir__())
        self.assertTrue('user_id' in new_review.__dir__())
        self.assertTrue('text' in new_review.__dir__())

    def test_review_attributes_are_strings(self):
        '''
        Checks that Review model's attributes are strings.
        '''
        new_review = Review()
        place_id = getattr(new_review, 'place_id')
        user_id = getattr(new_review, 'user_id')
        text = getattr(new_review, 'text')
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
