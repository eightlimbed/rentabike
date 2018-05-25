#!/usr/bin/python3
'''
This module contains the Base Model for all objects. Each object has the
following attributes and methods:

    Attributes:
    -----------
    `id`:         String
    `created_at`: Datetime
    `updated_at`: datetime

    Methods:
    --------
    `save(self)`:    Updates the objects `updated_at` attribute.
    `to_dict(self)`: Returns a dictionary of all key/values of the object's
                     __dict__ to JSON serialization.
'''
from datetime import datetime
import models
from sqlalchemy import String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

# SQLAlchemy's declarative base for Object Relational Mapping
Base = declarative_base()


class BaseModel:
    '''
    Base model for all objects. Every model will inherit from this class.

    Attributes:
    -----------
    `id`:         String
    `created_at`: Datetime
    `updated_at`: datetime

    Methods:
    --------
    `__init__(self, *args, **kwargs)`: Instance initializer.
    `save(self)`: Updates the objects `updated_at` attribute.
    `to_dict(self)`: Returns a dictionary of all key/values of the object's
                     __dict__ for JSON serialization.
    `__str__(self)`: Modifies string representation of an instance.
    `__repr__(self)`: Modifies string representation of an instance.

    '''

    # Class attributes for our database. These will represent Columns in the
    # table designated for that specific model (ex: State => `states`)
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        '''
        Initializes the BaseModel attributes and saves the object to storage.
        '''
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
        if kwargs:
            for key, val in kwargs.items():
                if '__class__' not in key:
                    setattr(self, key, val)

    def __str__(self):
        '''
        Modifies the string representation of each instance.
        '''
        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        '''
        Modifies the string representation of each instance.
        '''
        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
        Updates the updated_at attribute with current datetime and saves the
        object to storage.
        '''
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''
        Adds a `__class__` attribute to an instance's __dict__, converts
        datetime attributes to strings (for JSON serialization) and returns a
        dictionary representation of the instance.
        '''
        d = dict(self.__dict__)
        d['__class__'] = self.__class__.__name__
        d['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        d['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        # remove the key '_sa_instance_state' if it exists
        d = {k: v for k, v in d.items() if k != '_sa_instance_state'}
        return d

    def delete(self):
        '''
        Deletes an object by calling the object's storage.delete() method.
        '''
        models.storage.delete(self)
