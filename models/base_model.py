#!/usr/bin/python3
"""importing modules for the base class"""

import uuid
from datetime import datetime


class BaseModel:

    """init method"""

    def __init__(self, *args, **kwargs):

        """ class for base model updated for kwargs and args"""

        if kwargs is not None and args != {}:

            if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    """def str function"""
    def __str__(self):
        return '[__class__.__name__], (self.id), self.__dict__'

    """save function"""
    def save(self):
        self.updated_at = datetime.now()

    """save to dict"""
    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__

        if 'created_at' in my_dict:
            my_dict['created_at'] = my_dict['created_at'].isoformat()
        if 'updated_at' in my_dict:
            my_dict['updated_at'] = my_dict['updated_at'].isoformat()

        return my_dict
