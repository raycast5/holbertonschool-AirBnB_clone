#!/usr/bin/python3
"""Review class test"""

import unittest

import models
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for Review Class"""

    def test_inst_type(self):
        r1 = Review()
        self.assertEqual(Review, type(Review()))
        self.assertIsInstance(r1.user_id, str)
        self.assertIsInstance(r1.place_id, str)
        self.assertIsInstance(r1.text, str)

    def test_storage(self):
        self.assertIn(Review(), models.storage.all().values())
