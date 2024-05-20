#!/usr/bin/python3
"""
unittest for State module
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Testing all attributes and methods of State class"""

    def test_Is_instance(self):
        my_state = State()
        self.assertIsInstance(my_state, BaseModel)
        self.assertIs(State, type(my_state))
        self.assertIsInstance(my_state.id, str)
        self.assertIsInstance(my_state.created_at, datetime)
        self.assertIsInstance(my_state.updated_at, datetime)
        self.assertIsInstance(my_state.name, str)

    def test_State_unique_ID(self):
        state_1 = State()
        state_2 = State()
        self.assertNotEqual(state_1.id, state_2.id)

    def test_State_str_repres(self):
        my_state = State()
        output = "[State] ({}) {}".format(my_state.id, my_state.__dict__)
        self.assertEqual(my_state.__str__(), output)

    def test_State_save(self):
        my_state = State()
        old_created_date = my_state.created_at
        old_updated_date = my_state.updated_at
        my_state.save()
        new_updated_date = my_state.updated_at
        self.assertNotEqual(old_updated_date, new_updated_date)
        self.assertEqual(old_created_date, my_state.created_at)

    def test_State_to_dict(self):
        my_state = State()
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        my_state.name = "Alx"
        my_state.my_number = 89
        self.assertIn("id", my_state.to_dict())
        self.assertIn("created_at", my_state.to_dict())
        self.assertIn("updated_at", my_state.to_dict())
        self.assertIn("name", my_state.to_dict())
        self.assertIn("my_number", my_state.to_dict())
        self.assertIn("__class__", my_state.to_dict())
        self.assertNotEqual(my_state.__dict__, my_state.to_dict())
        self.assertEqual(my_state.to_dict()["created_at"],
                         my_state.created_at.strftime(d_format))
