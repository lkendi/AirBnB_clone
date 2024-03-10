#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):
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

    def test_to_dict(self):
        """Test State to_dict method"""
        state = State()
        state_dict = state.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertEqual(state_dict["__class__"], "State")
        self.assertTrue("id" in state_dict)
        self.assertTrue("created_at" in state_dict)
        self.assertTrue("updated_at" in state_dict)
        self.assertTrue("name" in state_dict)

    def test_from_dict(self):
        """Test State from_dict method"""
        state_dict = {
            "id": "123",
            "created_at": "2022-01-01T00:00:00",
            "updated_at": "2022-01-01T00:00:00",
            "name": "California"
        }
        state = State(**state_dict)
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(state.updated_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(state.name, "California")


if __name__ == "__main__":
    unittest.main()
