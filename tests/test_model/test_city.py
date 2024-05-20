#!/usr/bin/python3
"""
unittest for City module
"""
import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Testing all attributes and methods of City class"""

    def test_Is_Instance(self):
        my_city = City()
        self.assertIsInstance(my_city, BaseModel)
        self.assertIs(City, type(my_city))
        self.assertIsInstance(my_city.id, str)
        self.assertIsInstance(my_city.created_at, datetime)
        self.assertIsInstance(my_city.updated_at, datetime)
        self.assertIsInstance(my_city.state_id, str)
        self.assertIsInstance(my_city.name, str)

    def test_City_unique_ID(self):
        city_1 = City()
        city_2 = City()
        self.assertNotEqual(city_1.id, city_2.id)

    def test_City_str_repres(self):
        my_city = City()
        output = "[City] ({}) {}".format(my_city.id, my_city.__dict__)
        self.assertEqual(my_city.__str__(), output)

    def test_City_save(self):
        my_city = City()
        old_created_date = my_city.created_at
        old_updated_date = my_city.updated_at
        my_city.save()
        new_updated_date = my_city.updated_at
        self.assertNotEqual(old_updated_date, new_updated_date)
        self.assertEqual(old_created_date, my_city.created_at)

    def test_City_to_dict(self):
        my_city = City()
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        my_city.name = "Marrakesh"
        my_city.my_number = 89
        self.assertIn("id", my_city.to_dict())
        self.assertIn("created_at", my_city.to_dict())
        self.assertIn("updated_at", my_city.to_dict())
        self.assertIn("name", my_city.to_dict())
        self.assertIn("my_number", my_city.to_dict())
        self.assertIn("__class__", my_city.to_dict())
        self.assertNotEqual(my_city.__dict__, my_city.to_dict())
        self.assertEqual(my_city.to_dict()["created_at"],
                         my_city.created_at.strftime(d_format))
