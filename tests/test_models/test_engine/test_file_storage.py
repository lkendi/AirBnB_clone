#!/usr/bin/python3

"""
Unitest for file_storage.py
"""

import unittest
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Test for setup"""
        self.storage = FileStorage()

    def tearDown(self):
        """Test for teardown"""
        self.storage = None

    def test_all(self):
        """
        Test for alll
        """
        self.assertNotEqual(self.storage.all(), {})

    def test_new(self):
        """
        Test for new user
        """
        user = User()
        self.storage.new(user)
        self.assertIn(f"User.{user.id}", self.storage.all())

    def test_save(self):
        """
        Test for user being saved
        """
        user = User()
        self.storage.new(user)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, "r") as json_file:
            data = json.load(json_file)
            self.assertIn(f"User.{user.id}", data)

    def test_reload(self):
        """
        Test for user being reloaded
        """
        user = User()
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"User.{user.id}", self.storage.all())

    def test_classes(self):
        """Test for storage of other classes"""
        classes = self.storage.classes()
        self.assertEqual(classes, {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        })


if __name__ == "__main__":
    unittest.main()
