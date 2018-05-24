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
    `price_per_hour`: Int
'''

from models.base_model import BaseModel


class Bike(BaseModel):
    '''
    Bike model, which inherits from Base Model and contains a additional
    attributes: `city_id` (String), `user_id` (String), `latitude` (Float),
    `longitude` (Float), `name` (String), `description` (String), `color`
    (String), `size` (Float), `category_ids` (List), `price_per_day` (Int),
    and `price_per_hour` (Int)
    '''
    city_id = ''
    user_id = ''
    latitude = 0.0
    longitude = 0.0
    name = ''
    description = ''
    color = ''
    size = 0.0
    category_ids = []
    price_per_day = 0
    price_per_hour = 0
