#!/usr/bin/python3
"""City class test"""

import unittest

import models
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for City Class"""

    def test_inst_type(self):
        self.assertEqual(City, type(City()))

    def test_storage(self):
        self.assertIn(City(), models.storage.all().values())
