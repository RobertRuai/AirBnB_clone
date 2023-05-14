#!/usr/bin/python3
"""state class test module"""
import unittest
from models.state import State
from models.base_model import BaseModel


class testState(unittest.TestCase):
    """State test class."""

    def test_state(self):
        """Testing instances"""
        a = State()
        self.assertTrue(isinstance(a, State))
