#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.
    attributes:
        city_id (str): city id
        amenity_ids (list): list of amenity ids
        name (str): name of the place
        number_bathrooms (int): number of bathrooms
        max_guest (int): max number of guests
        price_by_night (int): price by night
        number_rooms (int): number of rooms
        user_id (str): user id
        latitude (float): latitude
        description (str): description of the place
        longitude (float): longitude
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
