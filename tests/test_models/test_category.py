#!/usr/bin/python3
'''
Unit tests for Category Model
'''
import datetime
from io import StringIO
from models.base_model import BaseModel
from models.category import Category
import unittest
import sys


class TestCategory(unittest.TestCase):
    '''
    Unit tests for Category Model.
    '''

    def test_category_inherits_from_base_model(self):
        '''
        Checks that the Category class Inherits from BaseModel
        '''
        new_category = Category()
        self.assertIsInstance(new_category, BaseModel)

    def test_category_has_attributes(self):
        '''
        Checks the category attributes exist
        '''
        new_category = Category()
        self.assertTrue('name' in new_category.__dir__())

    def test_name_attribute_is_a_string(self):
        '''
        Checks that `first_name` is a string.
        '''
        new = Category()
        name = getattr(new, 'name')
        self.assertIsInstance(name, str)
