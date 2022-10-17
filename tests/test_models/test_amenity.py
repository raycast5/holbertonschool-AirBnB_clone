#!/usr/bin/python3
"""Amenity class test"""

import unittest

import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for Amenity Class"""

    def test_inst_type(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_storage(self):
        self.assertIn(Amenity(), models.storage.all().values())
