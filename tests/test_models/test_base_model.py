#!/usr/bin/python3
"""Unittest module for BaseModel class
"""
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Tests the creation of a new instance
        with all arguments set correctly"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, "id"))
        self.assertIsInstance(obj.id, str)
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertIsInstance(obj.updated_at, datetime)

    def test_unique_id_assignment(self):
        """Test that each instance is unique/has a unique id"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1, obj2)
        self.assertNotEqual(obj1.id, obj2.id)

    def test_str_method(self):
        """Tests the str method"""
        obj = BaseModel()
        test_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), test_str)

    def test_save_method(self):
        """Tests the save method"""
        obj = BaseModel()
        first_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(first_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', obj_dict)
        self.assertIsInstance(datetime
                              .fromisoformat(obj_dict['created_at']), datetime)
        self.assertIn('updated_at', obj_dict)
        self.assertIsInstance(datetime
                              .fromisoformat(obj_dict['updated_at']), datetime)


if __name__ == "__main__":
    unittest.main()
