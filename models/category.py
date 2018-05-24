#!/usr/bin/python3
'''
This module contains the Category Model, which inherits from Base Model and
contains the following additional attribute:

    Attributes:
    -----------
    `name`: String
'''
from models.base_model import BaseModel


class Category(BaseModel):
    '''
    Category model, which inherits from Base Model and contains an additional
    attribute: `name` (String).
    '''
    name = ''
