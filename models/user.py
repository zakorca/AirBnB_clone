#!/usr/bin/python3

"""This is the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel
    Attributes:
        email (str): email addr
        password (str): passwrd
        first_name (str): f name
        last_name (str): L name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
