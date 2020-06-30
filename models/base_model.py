#!/usr/bin/python3
"""
BaseModel - Module

Parent class to take care of the initialization,
serialization and deserialization of instances
 """

import uuid
import datetime
import models


class BaseModel():
    """
    BaseModel class Parent class to take care of the initialization,
    serialization and deserialization of instances
    """
    def __init__(self, *args, **kwargs):
        """Initialization of a BaseModel instance"""
        if len(kwargs) != 0:
            for key in kwargs:
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        formato = "%Y-%m-%dT%H:%M:%S.%f"
                        d = datetime.datetime.strptime(kwargs[key], formato)
                        setattr(self, key, d)
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

        models.storage.new(self)

    def __str__(self):
        """String representation of a BaseModel instance"""
        msg = "[{}] ({}) {}"
        return msg.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updating BaseModel instance"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary representation of a BaseModel instance"""
        temp = self.__dict__.copy()
        temp["__class__"] = self.__class__.__name__
        temp["created_at"] = temp["created_at"].isoformat()
        temp["updated_at"] = temp["updated_at"].isoformat()
        return temp
