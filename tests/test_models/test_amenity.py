#!/usr/bin/python3
"""Amenity class test"""

import unittest

import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for Amenity Class"""

    def test_inst_type(self):
        a1 = Amenity()
        self.assertEqual(Amenity, type(Amenity()))
        self.assertIsInstance(a1.name, str)

    def test_storage(self):
        self.assertIn(Amenity(), models.storage.all().values())
