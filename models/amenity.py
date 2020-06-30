#!/usr/bin/python3
"""Amenity Module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ 
    Amenit Class
    Representation of Amenity in the platform
    """
    name = ""

    def __init__(self, *args **kwargs):
        """Initializes Amenity"""
        super().__init__(self, *args **kwargs)
