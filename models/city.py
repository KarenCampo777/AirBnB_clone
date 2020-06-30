#!/usr/bin/python3
"""City Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """ 
    City Class
    Representation of City in the platform
    """
    state_id = ""
    name = ""
    def __init__(self, *args **kwargs):
        """Initializes City"""
        super().__init__(self, *args **kwargs)
