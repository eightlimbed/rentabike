#!/usr/bin/python3
'''
Unit tests for City Model
'''
import datetime
from io import StringIO
from models.base_model import BaseModel
from models.city import City
import unittest
import sys


class TestCity(unittest.TestCase):
    '''
    Unit tests for City Model.
    '''

    def test_city_inherits_from_base_model(self):
        '''
        Checks that the City class Inherits from BaseModel
        '''
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_city_has_attributes(self):
        '''
        Checks the city attributes exist
        '''
        new_city = City()
        self.assertTrue('name' in new_city.__dir__())
        self.assertTrue('state_id' in new_city.__dir__())

    def test_name_attribute_is_a_string(self):
        '''
        Checks that `name` is a string.
        '''
        new = City()
        name = getattr(new, 'name')
        self.assertIsInstance(name, str)

    def test_state_id_attribute_is_a_string(self):
        '''
        Checks that `state_id` is a string.
        '''
        new = City()
        state_id = getattr(new, 'state_id')
        self.assertIsInstance(state_id, str)
