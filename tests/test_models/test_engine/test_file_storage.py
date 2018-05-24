#!/usr/bin/python3
'''
Unit tests for FileStorage class.
'''
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import time
import unittest


class TestFileStorage(unittest.TestCase):
    '''
    Unit tests for FileStorage class
    '''
    def setUp(self):
        '''
        Initializes instances of FileStorage and BaseModel for unit tests.
        '''
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        '''
        Removes JSON file after each test.
        '''
        try:
            os.remove("all_objects_data.json")
        except FileNotFoundError:
            pass

    def test_all_method_returns_a_dictionary(self):
        '''
        Tests the data type of the return value of `all()`.
        '''
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_new_method_sets_key_and_value(self):
        '''
        Tests that the new method sets the right key and value pair in the
        `FileStorage.__objects` dictionary.
        '''
        key = self.my_model.__class__.__name__ + "." + self.my_model.id
        self.assertFalse(key in self.storage._FileStorage__objects)
        self.storage.new(self.my_model)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_objects_class_name_is_correct(self):
        '''
        Tests that the type of an object's value contained in 
        `FileStorage.__object` is the object's `__class__.__name__`.
        '''
        self.storage.new(self.my_model)
        key = self.my_model.__class__.__name__ + "." + self.my_model.id
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.my_model, type(val))

    def test_save_method_creates_a_JSON_file(self):
        '''
        Tests that a JSON file gets created with the name all_objects_data.json.
        '''
        self.storage.save()
        self.assertTrue(os.path.isfile('all_objects_data.json'))

    def test_save_file_read(self):
        '''
        Checks that the contents of the JSON file is a dictionary.
        '''
        # Creates a new FileStorage() and BaseModel() in `setUp()`...
        self.storage.save()
        self.storage.new(self.my_model)
        with open('all_objects_data.json', 'r', encoding='utf-8') as f:
            content = json.load(f)
        self.assertTrue(type(content) is dict)

    def test_JSON_file_content_is_of_type_string(self):
        '''
        Checks that esting the type of the contents inside the file.
        '''
        # Creates a new FileStorage() and BaseModel() in `setUp()`...
        self.storage.save()
        self.storage.new(self.my_model)
        with open('all_objects_data.json', 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIsInstance(content, str)
