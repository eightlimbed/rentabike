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
from models.base_model import BaseModel


class User(BaseModel):
    '''
    User model, which inherits from Base Model and contains four additional
    attributes: `email`, `password`, `first_name` and `last_name` (all Strings).
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
