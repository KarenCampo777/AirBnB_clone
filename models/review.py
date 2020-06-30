#!/usr/bin/python3
"""Review Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ 
    Review Class
    Representation of Place in the platform
    """

    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args **kwargs):
        """Initializes Review"""
        super().__init__(self, *args **kwargs)