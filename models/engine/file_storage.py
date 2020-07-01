#!/usr/bin/python3
"""

file_storage - module

Handles the dictionary representation of an object to be
stored in a JSON file

"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():

    """
    FileStorage class

    Class used to handle the dictionary representation of an
    object to be stored in a JSON file.

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return all objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Set new obj into __objects
        """
        msg = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[msg] = obj

    def save(self):
        """
        Serializes the objects into JSON file
        """
        my_dict = {}
        for obj in self.__objects:
            my_dict[obj] = self.__objects[obj].to_dict()

        with open(self.__file_path, mode='w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        Reload the file and deserializes JSON into __objects
        """

        if os.access(self.__file_path, os.F_OK):
            with open(self.__file_path, mode='r') as f:
                j_file = json.load(f)
                for key, value in j_file.items():
                    obj = eval(value["__class__"])(**value)
                    self.__objects[key] = obj
