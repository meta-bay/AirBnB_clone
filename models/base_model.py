#!/usr/bin/python3
"""
    BaseMode module
"""


from uuid import uuid4
from datetime import datetime



class BaseModel:
    """ Base Model Class"""

    def __init__(self, *args, **kwargs):
        """ initializes the object"""
        if kwargs is not None and kwargs != {}:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(val))
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """string representation of the object """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save Time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ the dictionary """
        the_dict = self.__dict__.copy()
        the_dict['__class__'] = self.__class__.__name__
        the_dict['created_at'] = the_dict['created_at'].isoformat()
        the_dict['updated_at'] = the_dict['updated_at'].isoformat()
        return the_dict