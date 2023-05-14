#!/usr/bin/python3
"""City class test module"""
import unittest
from models.city import City
from models.base_model import BaseModel


class testCity(unittest.TestCase):
    """City test class."""

    def test_city(self):
        """Testing instances"""
        a = City()
        self.assertTrue(isinstance(a, City))
