#!/usr/bin/python3


"""
Test module for file_storage module
"""

from models.engine.file_storage import FileStorage
import models
import unittest
import os



class TestFileStorage(unittest.TestCase):
    """ Testing a FileStorage instance """

    def setUp(self):
        """
        Setting up the test instance
        """
        self.my_base1 = FileStorage()
        self.my_base2 = FileStorage()

    def Tearown(self):
        """
        Closing the test instance
        """
        del self.my_base1
        del self.my_base2

    def test_create(self):
        """
        Testing creation of a FileStorage engine instance
        """
        self.assertIsInstance(self.my_base1, FileStorage)

    def test_permissions(self):
        """
        Testing file permissions to be executable
        """
        self.assertTrue(os.access("models/engine/file_storage.py", os.X_OK))

    def test_docstring(self):
        """
        Testing documentation on file_storage
        """
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)
