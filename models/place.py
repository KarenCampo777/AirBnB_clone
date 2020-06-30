#!/usr/bin/python3
"""Place Module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ 
    Place Class
    Representation of Place in the platform
    """
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    name = ""

    def __init__(self, *args **kwargs):
        """Initializes Place"""
        super().__init__(self, *args **kwargs)

