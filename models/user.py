#!/usr/bin/python3
"""User Module"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class
    Representation of a user in the platform
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args **kwargs):
        """Initializes User"""
        super().__init__(self, *args **kwargs)
