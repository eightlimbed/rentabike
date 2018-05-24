#!/usr/bin/python3
'''
This module contains the FileStorage class which holds all the attributes and
methods for a JSON file storage engine.

    Attributes:
    -----------
    `__file_path`: The name of the json file to store objects
    `__objects`: A dictionary of all objects in storage

    Methods:
    --------
    `all(self)`: Returns all objects in storage.
    `new(self, obj)`: Places a new object in the storage engine.
    `save(self)`: Serializes the object to JSON and saves it to a file.
    `reload(self)`: Deserializes the JSON representation of the objects to
                    Python objects.
'''
import json
import models


class FileStorage:
    '''
    File storage engine class. Contains the following attributes and methods
    required for JSON serialization and deserialization of objects:

    Attributes:
    -----------
    `__file_path`: The name of the json file to store objects
    `__objects`: A dictionary of all objects in storage

    Methods:
    --------
    `all(self)`: Returns all objects in storage.
    `new(self, obj)`: Places a new object in the storage engine.
    `save(self)`: Serializes the object to JSON and saves it to a file.
    `reload(self)`: Deserializes the JSON representation of the objects to
                    Python objects.

    '''
    __file_path = 'all_objects_data.json'
    __objects = {}

    def all(self):
        '''
        Returns a dictionary containing all objects in storage.
        '''
        return self.__objects

    def new(self, obj):
        '''
        Creates a keystring and sets a new object in the `__objects` dictionary.
        '''
        key = obj.__class__.__name__ + "." + str(obj.id)
        val = obj
        FileStorage.__objects[key] = val

    def save(self):
        '''
        Serializes all objects in the `__objects` dictionary to JSON and saves
        it to a file (`__file_path`).
        '''
        d = {}
        for key, val in FileStorage.__objects.items():
            d[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(d, f)

    def reload(self):
        '''
        Deserializes the objects in a JSON file (`__file_path`) and places them
        in the `__objects` dictionary.
        '''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
            for key, val in FileStorage.__objects.items():
                class_name = val['__class__']
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
