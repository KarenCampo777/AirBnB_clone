#!/usr/bin/python3
"""State Module"""
from models.base_model import BaseModel


class State(BaseModel):
    """ 
    State Class
    Representation of state in the platform
    """

    name = ""
    def __init__(self, *args **kwargs):
        """Initializes State"""
        super().__init__(self, *args **kwargs)
