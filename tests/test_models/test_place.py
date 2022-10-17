#!/usr/bin/python3
"""Place class test"""

import unittest

import models
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for Place Class"""

    def test_inst_type(self):
        p1 = Place()
        self.assertEqual(Place, type(Place()))
        self.assertIsInstance(p1.city_id, str)
        self.assertIsInstance(p1.user_id, str)
        self.assertIsInstance(p1.name, str)
        self.assertIsInstance(p1.description, str)
        self.assertIsInstance(p1.number_bathrooms, int)
        self.assertIsInstance(p1.number_rooms, int)
        self.assertIsInstance(p1.max_guest, int)
        self.assertIsInstance(p1.price_by_night, int)
        self.assertIsInstance(p1.latitude, float)
        self.assertIsInstance(p1.longitude, float)
        self.assertIsInstance(p1.amenity_ids, list)

    def test_storage(self):
        self.assertIn(Place(), models.storage.all().values())
