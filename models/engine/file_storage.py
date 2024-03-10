#!/usr/bin/python3
"""
File Storage Module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class that serializes instances to JSON file
    and deserializes JSON file to instances

    Attributes:
    __file_path(str): path to JSON file
    __objects(dict): empty but will store all objects by <class name>.id

    Methods:
        all(self): returns the dictionary __objects
        new(self, obj):  sets in __objects the obj with key <obj class name>.id
        save(self):  serializes __objects to the JSON file
        reload(self): deserializes the JSON file to __objects (only if the JSON
                file (__file_path) exists ; otherwise, do nothing.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON filepath"""
        json_data = {}
        for k, v in FileStorage.__objects.items():
            json_data[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(json_data, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                json_data = json.load(json_file)
                for k, v in json_data.items():
                    FileStorage.__objects[k] = self.classes()[v["__class__"]](**v)
        except Exception:
            pass

    def classes(self):
        """More classes"""
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes
