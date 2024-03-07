#!/usr/bin/python3
"""
File Storage Module
"""

import json


class FileStorage:
    """Class that serialized instances to JSON file
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

    def __init__(self, file_path, objects):
        self.__file_path = file_path
        self.__objects = objects

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        #TODO: Add code

    def save(self):
        """Serializes __objects to the JSON filepath"""
        #TODO: Add code

    def reload(self):
        """Deserialized the JSON file to __objects"""
        #TODO: Add code
