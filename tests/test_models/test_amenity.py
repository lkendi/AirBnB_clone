import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_instance(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_inherited_from_base_model(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertIsInstance(self.amenity.name, str)

    def test_str(self):
            expected_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
            self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict(self):
            amenity_dict = self.amenity.to_dict()
            self.assertTrue(isinstance(amenity_dict, dict))
            self.assertEqual(amenity_dict["__class__"], "Amenity")
            self.assertTrue("name" in amenity_dict)

    def test_from_dict(self):
            amenity_dict = {
                "id": "123",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
                "name": "TV"
            }
            amenity = Amenity(**amenity_dict)
            self.assertEqual(amenity.id, "123")
            self.assertEqual(amenity.created_at.isoformat(), "2022-01-01T00:00:00")
            self.assertEqual(amenity.updated_at.isoformat(), "2022-01-01T00:00:00")
            self.assertEqual(amenity.name, "TV")


if __name__ == "__main__":
    unittest.main()
