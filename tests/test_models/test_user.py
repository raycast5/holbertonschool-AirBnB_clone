#!/usr/bin/python3
"""User class test"""

import unittest

import models
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for User Class"""

    def test_inst_type(self):
        self.assertEqual(User, type(User()))

    def test_storage(self):
        self.assertIn(User(), models.storage.all().values())
