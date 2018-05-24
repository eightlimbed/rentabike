#!/usr/bin/python3
'''
Unit tests for State Model
'''
import datetime
from io import StringIO
from models.base_model import BaseModel
from models.state import State
import unittest
import sys


class TestState(unittest.TestCase):
    '''
    Unit tests for State Model.
    '''

    def test_state_inherits_from_base_model(self):
        '''
        Checks that the State class Inherits from BaseModel
        '''
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_state_has_attributes(self):
        '''
        Checks the state attributes exist
        '''
        new_state = State()
        self.assertTrue('name' in new_state.__dir__())

    def test_name_attribute_is_a_string(self):
        '''
        Checks that `name` is a string.
        '''
        new = State()
        name = getattr(new, 'name')
        self.assertIsInstance(name, str)
