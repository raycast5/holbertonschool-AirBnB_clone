#!/usr/bin/python3
"""State class test"""

import unittest

import models
from models.state import State


class TestState(unittest.TestCase):
    """Tests for State Class"""

    def test_inst_type(self):
        s1 = State()
        self.assertEqual(State, type(State()))
        self.assertIsInstance(s1.name, str)

    def test_storage(self):
        self.assertIn(State(), models.storage.all().values())
