#!/usr/bin/python3
"""Place class test"""

import unittest

import models
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for Place Class"""

    def test_inst_type(self):
        self.assertEqual(Place, type(Place()))

    def test_storage(self):
        self.assertIn(Place(), models.storage.all().values())
