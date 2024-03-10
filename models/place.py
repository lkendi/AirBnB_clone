#!/usr/bin/python3
"""
Place class module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class - inherits from BaseModel

    Attributes:
        city_id(string): id of the city that the place belongs to
        user_id(string): id of the user who owns the place
        name(string): name of the place
        number_rooms(int): number of rooms in the place
        number_bathrooms(int): number of bathrooms in the place
        max_guest(int): max number of guests the place can accommodate
        price_by_night(int): nightly price for the place
        latitude(float): latitude coordinate
        longitude(float): longitude coordinate
        amenity_ids(list of str): list of amenity ids
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
