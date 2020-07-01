#!/usr/bin/python3

""" Unittest module for base_model module """

import unittest
import models
from models.base_model import BaseModel
import os
import datetime


class TestInitBaseModel(unittest.TestCase):
    """ Testing the initialization of a BaseModel instance """

    def setUp(self):
        """
        Setting up the test instance
        """
        self.my_base1 = BaseModel()
        self.my_base2 = BaseModel()

    def Tearown(self):
        """
        Closing the test instance
        """

    def test_create(self):
        """
        Testing creation of a BaseModel instance
        """
        self.assertIsInstance(self.my_base1, BaseModel)

    def test_permissions(self):
        """
        Testing file permissions to be executable
        """
        self.assertTrue(os.access("models/base_model.py", os.X_OK))

    def test_id(self):
        """
        Testing if attribute id is as unique as a string type
        """
        self.assertIsInstance(self.my_base1.id, str)
        self.assertNotEqual(self.my_base1.id, self.my_base2.id)

    def test_dates(self):
        """
        Testing created_at and updated_at of instances
        """
        self.assertIsInstance(self.my_base1.created_at, datetime)
        self.assertIsInstance(self.my_base1.updated_at, datetime)
        prev_date = self.my_base1.updated_at
        self.my_base1.save()
        self.assertIsEqual(prev_date, self.my_base1.updated_at)

    def test_str_format(self):
        """
        Testing the function __str__ to have the correct format
        [<class name>] (<self.id>) <self.__dict__>
        """
        o = self.my_base1
        msg1 = o.__str__()
        msg2 = "[{}] ({}) {}".format(o.__class__.__name__, o.id, o.__dict__)
        self.assertIsEqual(msg1, msg2)

    def test_to_dict(self):
        """
        Testing to_dict function to return correct format
        """
        ins = self.my_base1
        obj = ins.to_dict
        self.assertIsInstance(obj, dict)
        self.assertTrue('__class__' in obj)
        self.assertIsEqual(obj['__class__'], 'BaseModel')
        self.assertIsInstance(obj['created_at'], str)
        self.assertIsInstance(obj['updated_at'], str)
        self.assertIsEqual(obj['created_at'], ins.created_at.isoformat())
        self.assertIsEqual(obj['updated_at'], ins.updated_at.isoformat())

    def test_docstring(self):
        """
        Testing documentation on base_module
        """
        self.assertIsNotNone(models.base_model.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
