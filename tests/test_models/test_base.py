#!/usr/bin/python3
'''
Unit tests for Base Model
'''
from datetime import datetime
from io import StringIO
from models.base_model import BaseModel
import sys
import unittest


class TestBase(unittest.TestCase):
    '''
    Unit tests for Base Model.
    '''
    def setUp(self):
        '''
        Initializes an instance for unit tests.
        '''
        self.my_model = BaseModel()
        self.my_model.name = 'Theo'

    def TearDown(self):
        '''
        Removes the instance created by `setUp` after each test.
        '''
        del self.my_model

    def test_id_type_is_a_string(self):
        '''
        Checks that the type of the id is a string.
        '''
        self.assertEqual(str, type(self.my_model.id))

    def test_ids_are_different(self):
        '''
        Checks that the ids between two instances are different.
        '''
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_attribute_can_be_added(self):
        '''
        Checks that an attribute can be added.
        '''
        self.assertEqual('Theo', self.my_model.name)

    def test_updated_at_and_created_at_are_equal(self):
        '''
        Checks that both `created_at` and `updated_at` are equal at
        initialization
        '''
        self.assertEqual(self.my_model.updated_at.second,
                         self.my_model.created_at.second)

    def test_updated_at_is_different_after_save(self):
        '''
        Checks that `updated_at` is different than `created_at` after the
        `save()` method has been called.
        '''
        old_update = self.my_model.updated_at
        self.my_model.save()
        self.assertEqual(True, self.my_model.updated_at > old_update)

    def test_string_representation_meets_specifications(self):
        '''
        Checks that the string representation of each instance matches the
        format of: [<class name>] (<self.id>) <self.__dict__>
        '''
        backup = sys.stdout
        inst_id = self.my_model.id
        inst_dict = self.__dict__
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.my_model)
        cap = capture_out.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")
        self.assertEqual(cap[1], "({})".format(inst_id))

    def test_to_dict_type(self):
        '''
        Checks that the `to_dict()` method returns a dictionary.
        '''

        self.assertEqual(dict, type(self.my_model.to_dict()))

    def test_to_dict_has_a__class__key(self):
        '''
        Checks that the __class__ key exists after calling `to_dict()`
        '''
        self.assertEqual('BaseModel', self.my_model.to_dict().get('__class__'))

    def test_to_dict_type_updated_at_is_a_string(self):
        '''
        Checks that the type of `updated_at` after calling `to_dict()` is a
        string
        '''
        self.assertEqual(str, type((self.my_model.to_dict().get('updated_at'))))

    def test_to_dict_type_created_at_is_a_string(self):
        '''
        Checks that the type of `created_at` after calling `to_dict()` is a
        string
        '''
        self.assertEqual(str, type((self.my_model.to_dict().get('created_at'))))

    def test_instance_can_be_instantiated_using_kwargs(self):
        '''
        Checks that an instance can be created using kwargs.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, self.my_model.id)

    def test_created_at_is_a_datetime(self):
        '''
        Test that an instance's `created_at` attribute is a datetime object
        after instantiation (for deserialization)
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime))

    def test_updated_at_is_a_datetime(self):
        '''
        Test that an instance's `updated_at` attribute is a datetime object
        after instantiation (for deserialization)
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime))
