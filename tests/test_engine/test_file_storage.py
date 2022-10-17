#!/usr/bin/python3
"""Unittest for Base Class"""

import unittest

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b1 = FileStorage()
        cls.b2 = FileStorage()

    def test_init(self):
        """Test initialization"""
        self.b1.save()
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

    def test_to_dict(self):
        """Test that it saves a dict"""
        self.assertIsInstance(self.b1.to_dict(), dict)

    def test_id(self):
        """Test id"""
        self.assertNotEqual(self.b1.id, self.b2.id)
        self.assertIsInstance(self.b1.id, str)

    def test_str(self):
        """Test if __str__ returns str"""
        self.assertIsInstance(self.b1.__str__(), str)
