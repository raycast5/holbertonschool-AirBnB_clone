#!/usr/bin/python3
"""State class test"""

import unittest

import models
from models.state import State


class TestState(unittest.TestCase):
    """Tests for State Class"""

    def test_inst_type(self):
        self.assertEqual(State, type(State()))

    def test_storage(self):
        self.assertIn(State(), models.storage.all().values())
