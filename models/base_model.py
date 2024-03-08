#!/usr/bin/python3
"""BaseModel Module
"""

from datetime import datetime
from models.engine.file_storage import FileStorage
import uuid


class BaseModel:
    """BaseModel class

    Attributes:
        id (str): unique identifier for each instance
        created_at (datetime): time when the instance was created
        updated_at (datetime): time when the instance was last updated

    Methods:
        __init__: class constructor
        __str__: prints string description of an instance
        save: updates the updated_at attribute with the current datetime
        to_dict: returns a dictionary containing all keys/values
                    of __dict__ of the instance

    """

    def __init__(self, *args, **kwargs):
        """Constructor - initializes a new instance of the BaseModel class

        Args:
            created_at (date_time, optional): date and time of instance
                    creation. Default value of current date and time
            updated_at (date_time, optional): date and time when the instance
                    was last updated. Default value of current date and time
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime
                            .strftime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            FileStorage().new(self)

    def __str__(self):
        """Returs a string representation of an instance"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current date and time
        and saves the current object to the file storage"""
        self.updated_at = datetime.now()
        FileStorage().save()

    def to_dict(self):
        """Converts an instance to a dictionary

        Returns:
            obj_dict: dictionary containing all attributes of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
