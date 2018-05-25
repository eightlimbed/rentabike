#!/usr/bin/python3
'''
This module contains the Review Model, which inherits from Base Model and
contains the following additional attributes:

    Attributes:
    -----------
    `place_id`: String
    `user_id`: String
    `text`: String
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


class Review(BaseModel, Base):
    '''
    Review model, which inherits from Base Model and contains an additional
    attributes: `place_id`, `user_id`, and `text` (all strings).
    '''
    __tablename__ = 'reviews'
    bike_id = Column(String(60), ForeignKey('bikes.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
