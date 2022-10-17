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

class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b1 = BaseModel()
        cls.b2 = BaseModel()

    def test_init(self):
        """Test initialization"""
        original_date = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(original_date, self.b1.updated_at)
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
