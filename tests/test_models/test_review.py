import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_instance(self):
        self.assertIsInstance(self.review, Review)

    def test_inherited_from_base_model(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_default_attribute_values(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_str(self):
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertTrue(isinstance(review_dict, dict))
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertTrue("place_id" in review_dict)
        self.assertTrue("user_id" in review_dict)
        self.assertTrue("text" in review_dict)

    def test_from_dict(self):
        review_dict = {
            "id": "123",
            "created_at": "2022-01-01T00:00:00",
            "updated_at": "2022-01-01T00:00:00",
            "place_id": "456",
            "user_id": "789",
            "text": "This is a review."
        }
        review = Review(**review_dict)
        self.assertEqual(review.id, "123")
        self.assertEqual(review.created_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(review.updated_at.isoformat(), "2022-01-01T00:00:00")
        self.assertEqual(review.place_id, "456")
        self.assertEqual(review.user_id, "789")
        self.assertEqual(review.text, "This is a review.")


if __name__ == "__main__":
    unittest.main()
