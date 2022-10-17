#!/usr/bin/python3
"""Review class test"""

import unittest

import models
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for Review Class"""

    def test_inst_type(self):
        self.assertEqual(Review, type(Review()))

    def test_storage(self):
        self.assertIn(Review(), models.storage.all().values())
