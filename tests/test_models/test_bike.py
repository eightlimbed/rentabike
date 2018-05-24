#!/usr/bin/python3
'''
Unit tests for Bike Model
'''
import datetime
from io import StringIO
from models.base_model import BaseModel
from models.bike import Bike
import sys
import unittest


class TestBike(unittest.TestCase):
    '''
    Unit tests for Bike Model.
    '''

    def test_bike_inherits_from_base_model(self):
        '''
        Checks that the Bike class Inherits from BaseModel
        '''
        new_bike = Bike()
        self.assertIsInstance(new_bike, BaseModel)

    def test_bike_has_attributes(self):
        '''
        Checks the bike attributes exist
        '''
        new_bike = Bike()
        self.assertTrue('city_id' in new_bike.__dir__())
        self.assertTrue('user_id' in new_bike.__dir__())
        self.assertTrue('latitude' in new_bike.__dir__())
        self.assertTrue('longitude' in new_bike.__dir__())
        self.assertTrue('longitude' in new_bike.__dir__())
        self.assertTrue('name' in new_bike.__dir__())
        self.assertTrue('description' in new_bike.__dir__())
        self.assertTrue('color' in new_bike.__dir__())
        self.assertTrue('size' in new_bike.__dir__())
        self.assertTrue('category_ids' in new_bike.__dir__())
        self.assertTrue('price_per_day' in new_bike.__dir__())
