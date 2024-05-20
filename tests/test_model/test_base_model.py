#!/usr/bin/python3
"""
unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Testing all attributes and methods of BaseModel class"""

    def test_is_instances(self):
        bm = BaseModel()
        self.assertIs(BaseModel, type(bm))
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_unique_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at_two_instances(self):
        bm1 = BaseModel()
        time.sleep(0.2)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_str_repres(self):
        bm = BaseModel()
        output = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(bm.__str__(), output)

    def test_save(self):
        bm = BaseModel()
        old_created_date = bm.created_at
        old_updated_date = bm.updated_at
        bm.save()
        new_updated_date = bm.updated_at
        self.assertNotEqual(old_updated_date, new_updated_date)
        self.assertEqual(old_created_date, bm.created_at)

    def test_to_dict(self):
        bm = BaseModel()
        bm.name = "My First Model"
        bm.my_number = 91
        my_dict = bm.to_dict()
        self.assertTrue(dict, my_dict)
        self.assertIn("id", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("__class__", my_dict)
        self.assertIn("name", my_dict)
        self.assertIn("my_number", my_dict)
