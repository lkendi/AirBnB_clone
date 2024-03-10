#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_instance(self):
        self.assertIsInstance(self.user, User)

    def test_inherited_from_base_model(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, "id"))  # Inherited attributes
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "email"))  # Specific to User
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertIsInstance(self.user.email, str)  # Check attribute types
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_str(self):
        expected_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)


if __name__ == "__main__":
    unittest.main()
