#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return '[__class__.__name__], (self.id), self.__dict__'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__

        if 'created_at' in my_dict:
            my_dict['created_at'] = my_dict['created_at'].isoformat()
        if 'updated_at' in my_dict:
            my_dict['updated_at'] = my_dict['updated_at'].isoformat()

        return my_dict
