#!/usr/bin/python3
'''
This module contains the User Model, which inherits from Base Model and contains
the following additional attributes:

    Attributes:
    -----------
    `email`: String
    `password`: String
    `first_name`: String
    `last_name`: String
'''
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship, backref

class User(BaseModel, Base):
    '''
    User model, which inherits from Base Model and contains four additional
    attributes: `email`, `password`, `first_name` and `last_name` (all Strings).
    Maps with the database table 'users'.
    '''
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    bikes = relationship('Bike', cascade='all, delete', backref='user')
    reviews = relationship('Review', cascade='all, delete', backref='user')
