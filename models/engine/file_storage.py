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
from models import base_model, category, city, bike, review, state, user


class FileStorage:
    '''
    File storage engine class. Contains the necessary attributes and methods
    required for JSON serialization and deserialization of objects.
    '''
    CNC = {
        'BaseModel': base_model.BaseModel,
        'Category': category.Category,
        'City': city.City,
        'Bike': bike.Bike,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }
    __file_path = 'all_objects_data.json'
    __objects = {}

    def all(self, cls=None):
        '''
        Returns all objects. The format depends on the value of the
        environment variable 'HBNB_TYPE_STORAGE'. If it is 'file', this
        method will return a dictionary of objects that have been formatted
        using the `new()` method. If it is 'db', a list of all objects in
        the MySQL database will be returned.
        '''
        if cls:
            obj_dict = {}
            for key, value in self.__objects.items():
                if cls.__name__ in key:
                    obj_dict[key] = value
            return obj_dict
        else:
            return self.__objects

    def new(self, obj):
        '''
        Creates a keystring and sets a new object in the `__objects` dictionary.
        '''
        key = obj.__class__.__name__ + '.' + str(obj.id)
        FileStorage.__objects[key] = obj

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
        path = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(path, 'r', encoding='utf-8') as f:
                new_objs = json.load(f)
        except:
            return
        for o_id, d in new_objs.items():
            k_cls = d['__class__']
            FileStorage.__objects[o_id] = FileStorage.CNC[k_cls](**d)

    def delete(self, obj=None):
        '''
        Deletes an object from `FileStorage.__objects` if it exists.
        '''
        if obj is None:
            return
        FileStorage.__objects = {k: v for k, v in FileStorage.__objects.items()
                                 if v.id != obj.id}

    def close(self):
        '''
        Reloads the objects from the JSON file and places them in __objects.
        '''
        self.reload()
