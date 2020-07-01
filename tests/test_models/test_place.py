#!/usr/bin/python3

"""
Test module for place module
"""

from models.place import Place
import models
import unittest
import os
import datetime


class TestPlace(unittest.TestCase):
    """ Testing an Place instance """

    def setUp(self):
        """
        Setting up the test instance
        """
        self.my_base1 = Place()
        self.my_base2 = Place()

    def Tearown(self):
        """
        Closing the test instance
        """
        del self.my_base1
        del self.my_base2

    def test_create(self):
        """
        Testing creation of an Place instance
        """
        self.assertIsInstance(self.my_base1, Place)

    def test_permissions(self):
        """
        Testing file permissions to be executable
        """
        self.assertTrue(os.access("models/place.py", os.X_OK))

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
        self.assertIsInstance(self.my_base1.created_at, datetime.datetime)
        self.assertIsInstance(self.my_base1.updated_at, datetime.datetime)
        prev_date = self.my_base1.updated_at
        self.my_base1.save()
        self.assertNotEqual(prev_date, self.my_base1.updated_at)

    def test_str_format(self):
        """
        Testing the function __str__ to have the correct format
        [<class name>] (<self.id>) <self.__dict__>
        """
        o = self.my_base1
        msg1 = o.__str__()
        msg2 = "[{}] ({}) {}".format(o.__class__.__name__, o.id, o.__dict__)
        self.assertEqual(msg1, msg2)

    def test_to_dict(self):
        """
        Testing to_dict function to return correct format
        """
        ins = self.my_base1
        obj = ins.to_dict()
        self.assertIsInstance(obj, dict)
        self.assertTrue('__class__' in obj)
        self.assertEqual(obj['__class__'], 'Place')
        self.assertIsInstance(obj['created_at'], str)
        self.assertIsInstance(obj['updated_at'], str)
        self.assertEqual(obj['created_at'], ins.created_at.isoformat())
        self.assertEqual(obj['updated_at'], ins.updated_at.isoformat())

    def test_docstring(self):
        """
        Testing documentation on place
        """
        self.assertIsNotNone(models.place.__doc__)
        self.assertIsNotNone(Place.__doc__)
