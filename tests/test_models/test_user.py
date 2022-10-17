#!/usr/bin/python3
"""User class test"""

import unittest

import models
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for User Class"""

    def test_inst_type(self):
        u1 = User()
        self.assertEqual(User, type(User()))
        self.assertIsInstance(u1.email, str)
        self.assertIsInstance(u1.password, str)
        self.assertIsInstance(u1.first_name, str)
        self.assertIsInstance(u1.last_name, str)

    def test_storage(self):
        self.assertIn(User(), models.storage.all().values())
