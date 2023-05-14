#!/usr/bin/python3
"""Place class test module"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class testPlace(unittest.TestCase):
    """Place test class."""

    def test_place(self):
        """Testing instances"""
        a = Place()
        self.assertTrue(isinstance(a, Place))
