#!/usr/bin/python3
"""
File Storage Module
"""
import json


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
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON filepath"""
        json_data = {}
        for k, obj in self.__objects.items():
            json_data[k] = obj.to_dict()
        with open(self.__file_path, "a") as json_file:
            json.dump(json_data, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as json_file:
                json_data = json.load(json_file)
                for k, v in json_data.items():
                    class_name, obj_id = k.split('.')
                    mod_name = "models." + class_name.lower()
                    cls = getattr(__import__(mod_name, fromlist=[class_name]),class_name)
                    self.__objects[k] = cls(**v)
        except:
            pass
