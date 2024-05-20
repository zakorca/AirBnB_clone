#!/usr/bin/python3

"""
Defines Amenity module
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.
        attributes:
            name (str): name of the amenity
    """
    name = ""
