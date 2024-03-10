#!/usr/bin/python3
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    def test_instance(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_inherited_from_base_model(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Test State attributes"""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))

    def test_name(self):
        """Test State name attribute"""
        state = State()
        self.assertEqual(state.name, "")

    def test_str(self):
        """Test State __str__ method"""
        state = State()
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)


if __name__ == "__main__":
    unittest.main()
