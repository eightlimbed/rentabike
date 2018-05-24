#!/usr/bin/python3
'''
Unit tests for User Model
'''
import datetime
from io import StringIO
from models.base_model import BaseModel
from models.user import User
import unittest
import sys


class TestUser(unittest.TestCase):
    '''
    Unit tests for User Model.
    '''

    def test_user_inherits_from_base_model(self):
        '''
        Checks that the User class Inherits from BaseModel
        '''
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_user_has_attributes(self):
        '''
        Checks the user attributes exist
        '''
        new_user = User()
        self.assertTrue('email' in new_user.__dir__())
        self.assertTrue('first_name' in new_user.__dir__())
        self.assertTrue('last_name' in new_user.__dir__())
        self.assertTrue('password' in new_user.__dir__())

    def test_email_attribute_is_a_string(self):
        '''
        Checks that `email` is a string.
        '''
        new = User()
        name = getattr(new, 'email')
        self.assertIsInstance(name, str)

    def test_first_name_attribute_is_a_string(self):
        '''
        Checks that `first_name` is a string.
        '''
        new = User()
        name = getattr(new, 'first_name')
        self.assertIsInstance(name, str)

    def test_last_name_attribute_is_a_string(self):
        '''
        Checks that `last_name` is a string.
        '''
        new = User()
        name = getattr(new, 'last_name')
        self.assertIsInstance(name, str)

    def test_password_attribute_is_a_string(self):
        '''
        Checks that `password` is a string.
        '''
        new = User()
        name = getattr(new, 'password')
        self.assertIsInstance(name, str)
