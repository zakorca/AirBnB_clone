#!/usr/bin/python3
"""
unittest for Review module
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Testing all attributes and methods of Review class"""

    def test_Is_Instance(self):
        rv = Review()
        self.assertIsInstance(rv, BaseModel)
        self.assertIs(Review, type(rv))
        self.assertIsInstance(rv.id, str)
        self.assertIsInstance(rv.created_at, datetime)
        self.assertIsInstance(rv.updated_at, datetime)
        self.assertIsInstance(rv.place_id, str)
        self.assertIsInstance(rv.user_id, str)
        self.assertIsInstance(rv.text, str)

    def test_Review_unique_ID(self):
        rv_1 = Review()
        rv_2 = Review()
        self.assertNotEqual(rv_1.id, rv_2.id)

    def test_Review_str_repres(self):
        rv = Review()
        output = "[Review] ({}) {}".format(rv.id, rv.__dict__)
        self.assertEqual(rv.__str__(), output)

    def test_Review_save(self):
        rv = Review()
        old_created_date = rv.created_at
        old_updated_date = rv.updated_at
        rv.save()
        new_updated_date = rv.updated_at
        self.assertNotEqual(old_updated_date, new_updated_date)
        self.assertEqual(old_created_date, rv.created_at)

    def test_Review_to_dict(self):
        rv = Review()
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        rv.text = "I like the place"
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self.assertIn("text", rv.to_dict())
        self.assertIn("__class__", rv.to_dict())
        self.assertNotEqual(rv.__dict__, rv.to_dict())
        self.assertEqual(rv.to_dict()["updated_at"],
                         rv.updated_at.strftime(d_format))
