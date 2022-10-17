#!/usr/bin/python3
"""Unittest for Base Class"""

import unittest

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b0 = FileStorage()
        cls.b1 = FileStorage()
        cls.b2 = BaseModel()

    def test_new(self):
        """Test New"""
        models.storage.new(self.b2)
        fullname = "BaseModel." + self.b2.id
        self.assertIn(fullname, models.storage.all().keys())
        self.assertIn(self.b2, models.storage.all().values())

    def test_save(self):
        """Test Save"""
        models.storage.new(self.b2)
        models.storage.save()
        self.b2.save()
        fullname = "BaseModel." + self.b2.id
        with open("file.json", "r") as f:
            self.assertIn(fullname, f.read())

    def test_all(self):
        """Test if all returns dict"""
        self.assertIsInstance(self.b1.all(), dict)

    def test_init(self):
        """Tests initialization"""
        self.assertEqual(BaseModel, type(BaseModel()))
        self.assertEqual(type(models.storage), FileStorage)

    def test_attr(self):
        """Test file storage attributes"""
        self.assertIsInstance(self.b0.get_file_path(), str)
        self.assertEqual(self.b0.get_file_path(), "file.json")
        self.assertIsInstance(self.b0.get_objects(), dict)

    def test_reload(self):
        """ Check the reload() method."""
        self.b0.save()
        self.b0.reload()
        fullname = "BaseModel." + self.b2.id
        ob_dict = self.b0.all()
        self.assertFalse(ob_dict[fullname] is self.b2)
