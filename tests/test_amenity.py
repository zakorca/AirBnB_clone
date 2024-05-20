#!/usr/bin/python3
"""
unittest for Amenity module
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Testing all attributes and methods of Amenity class"""

    def test_Is_Instance(self):
        amnty = Amenity()
        self.assertIsInstance(amnty, BaseModel)
        self.assertIs(Amenity, type(amnty))
        self.assertIsInstance(amnty.id, str)
        self.assertIsInstance(amnty.created_at, datetime)
        self.assertIsInstance(amnty.updated_at, datetime)
        self.assertIsInstance(amnty.name, str)

    def test_Amenity_unique_ID(self):
        amnty_1 = Amenity()
        amnty_2 = Amenity()
        self.assertNotEqual(amnty_1.id, amnty_2.id)

    def test_Amenity_str_repres(self):
        amnty = Amenity()
        output = "[Amenity] ({}) {}".format(amnty.id, amnty.__dict__)
        self.assertEqual(amnty.__str__(), output)

    def test_Amenity_save(self):
        amnty = Amenity()
        old_created_date = amnty.created_at
        old_updated_date = amnty.updated_at
        amnty.save()
        new_updated_date = amnty.updated_at
        self.assertNotEqual(old_updated_date, new_updated_date)
        self.assertEqual(old_created_date, amnty.created_at)

    def test_Amenity_to_dict(self):
        amnty = Amenity()
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        amnty.name = "amenity"
        amnty.my_number = 89
        self.assertIn("id", amnty.to_dict())
        self.assertIn("created_at", amnty.to_dict())
        self.assertIn("updated_at", amnty.to_dict())
        self.assertIn("name", amnty.to_dict())
        self.assertIn("my_number", amnty.to_dict())
        self.assertIn("__class__", amnty.to_dict())
        self.assertNotEqual(amnty.__dict__, amnty.to_dict())
        self.assertEqual(amnty.to_dict()["created_at"],
                         amnty.created_at.strftime(d_format))
