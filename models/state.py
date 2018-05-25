#!/usr/bin/python3
'''
This module contains the State Model, which inherits from Base Model and
contains the following additional attribute:

    Attributes:
    -----------
    `name`: String
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import os


class State(BaseModel, Base):
    '''
    Defines the class State that inherits from BaseModel and Base, the
    declarative base from SQLAlchemy.
    State objects will be mapped to a MySQL table called 'states'
    Since State objects inherit from BaseModel, they will have access to
    the following Columns:
        `BaseModel.id`
        `BaseModel.created_at`
        `BaseModel.updated_at`
    '''
    if os.getenv('RENTABIKE_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            '''
            Getter method that returns the list of City instances for
            FileStorage engine.
            '''
            city_list = []
            all_cities = models.storage.all()
            for key, value in all_cities.items():
                try:
                    if self.id == value.state_id:
                        city_list.append(value)
                except AttributeError:
                    pass
            return city_list

    else:
        cities = relationship('City', cascade='all, delete', backref='state')
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
