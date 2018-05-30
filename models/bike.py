#!/usr/bin/python3
'''
This module contains the Bike Model, which inherits from Base Model and
contains the following additional attributes:

    Attributes:
    -----------
    `city_id`: String
    `user_id`: String
    `latitude`: Float
    `longitude`: Float
    `name`: String
    `description`: String
    `color`: String
    `size`: Float
    `category_ids`: List
    `price_per_day`: Int
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, Float, String, Column, DateTime
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship, backref


bike_category = Table('bike_category', Base.metadata,
                      Column('bike_id', String(60), ForeignKey('bikes.id'),
                             nullable=False),
                      Column('category_id', String(60),
                             ForeignKey('categories.id'),
                             nullable=False))


class Bike(BaseModel, Base):
    '''
    Bike model, which inherits from Base Model and contains a additional
    attributes: `city_id` (String), `user_id` (String), `latitude` (Float),
    `longitude` (Float), `name` (String), `description` (String), `color`
    (String), `size` (Float), `category_ids` (List), and `price_per_day` (Int).
    '''
    @property
    def reviews(self):
        '''
        Getter method that returns the list of Review instances for a Bike.
        '''
        review_list = []
        for review in self.reviews:
            if self.id == review.place_id:
                review_list.append(review)
        return review_list

    @property
    def categories(self):
        '''
        Getter method that returns the list of Category instances for a Bike.
        '''
        return self.category_ids

    @categories.setter
    def categories(self, obj):
        '''
        Setter method that handles appending Category instances to a list.
        If `val` is not a Category object, it won't be appended to the list.
        '''
        for categories in self.categories:
            if self.id == categories.place_id and \
                    obj.__class__.__name__ == 'Category':
                category_ids.append(obj)

    __tablename__ = 'bikes'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    img_url = Column(String(512))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    price_per_day = Column(Integer, nullable=False, default=0)
    category_ids = []
    reviews = relationship('Review', cascade='all, delete', backref='bike')
    categories = relationship('Category', secondary=bike_category,
                             viewonly=False)
