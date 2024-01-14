#!/usr/bin/python3
''' City Module '''
from models.base_model import BaseModel


class City(BaseModel):
    ''' city class that inherits form the BaseModel '''
    state_id = ''
    name = ''
