import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_instance(self):
        self.assertIsInstance(self.place, Place)

    def test_inherited_from_base_model(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_default_attribute_values(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_str(self):
        expected_str = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertTrue(isinstance(place_dict, dict))
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertTrue("city_id" in place_dict)
        self.assertTrue("user_id" in place_dict)
        self.assertTrue("name" in place_dict)
        self.assertTrue("description" in place_dict)
        self.assertTrue("number_rooms" in place_dict)
        self.assertTrue("number_bathrooms" in place_dict)
        self.assertTrue("max_guest" in place_dict)
        self.assertTrue("price_by_night" in place_dict)
        self.assertTrue("latitude" in place_dict)
        self.assertTrue("longitude" in place_dict)
        self.assertTrue("amenity_ids" in place_dict)

    def test_from_dict(self):
        place_dict = {
            "id": "123",
            "created_at": "2022-01-01T00:00:00",
            "updated_at": "2022-01-01T00:00:00",
            "city_id": "456",
            "user_id": "789",
            "name": "Cozy Cottage",
            "description": "A beautiful cottage in the countryside",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "amenity_ids": ["a1", "a2", "a3"]
        }
        place = Place(**place_dict)
        self.assertEqual(place.id, "123")
        self.assertEqual(place.created_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(place.updated_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(place.city_id, "456")
        self.assertEqual(place.user_id, "789")
        self.assertEqual(place.name, "Cozy Cottage")
        self.assertEqual(place.description, "A beautiful cottage in the countryside")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["a1", "a2", "a3"])


if __name__ == "__main__":
    unittest.main()
