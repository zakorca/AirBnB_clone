#!/usr/bin/python3
"""
unittest for User class
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Testing all attributes and methods of User class"""

    def test_is_instance(self):
        u = User()
        self.assertIsInstance(u, BaseModel)
        self.assertIs(User, type(u))
        self.assertIsInstance(u.id, str)
        self.assertIsInstance(u.created_at, datetime)
        self.assertIsInstance(u.updated_at, datetime)
        self.assertIsInstance(u.first_name, str)
        self.assertIsInstance(u.last_name, str)
        self.assertIsInstance(u.email, str)
        self.assertIsInstance(u.password, str)

    def test_user_unique_id(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_str_repres(self):
        u = User()
        output = "[User] ({}) {}".format(u.id, u.__dict__)
        self.assertEqual(u.__str__(), output)

    def test_user_save(self):
        u = User()
        old_created_date = u.created_at
        old_updated_date = u.updated_at
        u.save()
        new_updated_date = u.updated_at
        self.assertNotEqual(old_updated_date, new_updated_date)
        self.assertEqual(old_created_date, u.created_at)

    def test_user_to_dict(self):
        u = User()
        u.first_name = "Hajar"
        u.last_name = "Olivery"
        u.email = "airbnb@mail.com"
        u.password = "root"
        self.assertTrue(dict, u.to_dict())
        self.assertIn("id", u.to_dict())
        self.assertIn("created_at", u.to_dict())
        self.assertIn("updated_at", u.to_dict())
        self.assertIn("first_name", u.to_dict())
        self.assertIn("last_name", u.to_dict())
        self.assertIn("email", u.to_dict())
        self.assertIn("password", u.to_dict())
