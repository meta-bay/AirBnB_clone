#!/usr/bin/python3
'''
    base model module
'''
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    ''' Base model class '''

    def __init__(self, *args, **kwargs):
        ''' initializes the object '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        ''' string representation of the object '''
        return "[{}] ({}) {}".format(
            __class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' saves the time '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' to dictionary '''
        the_dict = self.__dict__.copy()
        the_dict["__class__"] = self.__class__.__name__
        the_dict["created_at"] = self.created_at.isoformat()
        the_dict["updated_at"] = self.updated_at.isoformat()
        return the_dict
