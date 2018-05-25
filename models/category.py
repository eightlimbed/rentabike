#!/usr/bin/python3
'''
This module contains the Category Model, which inherits from Base Model and
contains the following additional attribute:

    Attributes:
    -----------
    `name`: String
'''
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from models.bike import bike_category
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    '''
    Category model, which inherits from Base Model and contains an additional
    attribute: `name` (String).
    '''
    __tablename__ = 'categories'
    name = Column(String(128), nullable=False)
    bike_categories = relationship('Bike', secondary=bike_category)
