#!/usr/bin/python3
import uuid
from datetime import datetime
from datetime import timedelta
''' base model module'''


class BaseModel():
    ''' Base model class '''
    def __init__(self):
        ''' initializes the object '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        ''' saves the time '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' to dictionary '''
        the_dict = self.__dict__.copy()
        the_dict["__class__"] = __class__.__name__
        the_dict["id"] = self.id
        the_dict["created_at"] = self.created_at.isoformat()
        the_dict["updated_at"] = self.updated_at.isoformat()
        return the_dict
