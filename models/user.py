#!/usr/bin/python3s
'''
    The users module
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''user class that inherits from the BaseModel'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
