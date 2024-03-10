import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_instance(self):
        self.assertIsInstance(self.city, City)

    def test_inherited_from_base_model(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_default_attribute_values(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_str(self):
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertEqual(city_dict["__class__"], "City")
        self.assertTrue("state_id" in city_dict)
        self.assertTrue("name" in city_dict)

    def test_from_dict(self):
        city_dict = {
            "id": "123",
            "created_at": "2022-01-01T00:00:00",
            "updated_at": "2022-01-01T00:00:00",
            "state_id": "456",
            "name": "New York"
        }
        city = City(**city_dict)
        self.assertEqual(city.id, "123")
        self.assertEqual(city.created_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(city.updated_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(city.state_id, "456")
        self.assertEqual(city.name, "New York")


if __name__ == "__main__":
    unittest.main()
