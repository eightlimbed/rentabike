#!/usr/bin/python3
'''
This module contains the City Model, which inherits from Base Model and
contains the following additional attribute:

    Attributes:
    -----------
    `name`: String
    `state_id`: String
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    City model, which inherits from Base Model and contains two additional
    attributes: `state_id` and `name` (all Strings).
    '''
    state_id = ''
    name = ''
