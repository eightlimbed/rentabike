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

from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Review model, which inherits from Base Model and contains an additional
    attribute: `name` (String).
    '''
    place_id = ''
    user_id = ''
    text = ''
