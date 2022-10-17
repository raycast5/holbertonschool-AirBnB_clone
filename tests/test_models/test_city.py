#!/usr/bin/python3
"""City class test"""

import unittest

import models
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for City Class"""

    def test_inst_type(self):
        c1 = City()
        self.assertEqual(City, type(City()))
        self.assertIsInstance(c1.name, str)
        self.assertIsInstance(c1.state_id, str)

    def test_storage(self):
        self.assertIn(City(), models.storage.all().values())
