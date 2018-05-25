#!/usr/bin/python3
'''
This module contains the City Model, which inherits from Base Model and
contains the following additional attribute:

    Attributes:
    -----------
    `name`: String
    `state_id`: String
'''
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(BaseModel, Base):
    '''
    Defines the class City that inherits from BaseModel and Base, the
    declarative base from SQLAlchemy.
    City objects will be mapped to a MySQL table called 'cities'
    Since City objects inherit from BaseModel, they will have access to the
    following Columns:
        `BaseModel.id`
        `BaseModel.created_at`
        `BaseModel.updated_at`
    There is a relationship() between City and State. The relationship is
    defined in the State class. The `backref='state'` parameter establishes
    a `state` attribute in this class. So each City will have a `state`
    parameter. For example, if California has a state_id of 1, and you make
    a City with a state_id of 1, you can access the name of your City's
    state using `City.state.name`.
    '''
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    bikes = relationship('Bike', cascade='all, delete', backref='cities')
