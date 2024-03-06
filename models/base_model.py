#!/usr/bin/python3
"""BaseModel Module
"""


import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class

    Attributes:
        id (str, public): unique identifier for each instance
        created_at (datetime, public): time when the instance was created
        updated_at (datetime, public): time when the instance was last updated

    Methods:
        __init__: class constructor
        __str__: prints string description of an instance
        save: updates the updated_at attribute with the current datetime
        to_dict: returns a dictionary containing all keys/values
                    of __dict__ of the instance

    """

    def __init__(self, id=None, created_at=None, updated_at=None, *args, **kwargs):
        """Constructor - initializes a new instance of the BaseModel class

        Args:
            created_at (date_time, optional): date and time of instance
                    creation. Default value of current date and time
            updated_at (date_time, optional): date and time when the instance
                    was last updated. Default value of current date and time
        """
        for key, value in kwargs.items():
                if key == "created_at" or "updated_at":
                    setattr(self, key, datetime.strftime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = created_at or datetime.now()
            self.updated_at = updated_at or datetime.now()

    def __str__(self):
        """Returs a string representation of an instance"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current date and time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts an instance to a dictionary

        Returns:
            dict: dictionary containing all attributes of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
