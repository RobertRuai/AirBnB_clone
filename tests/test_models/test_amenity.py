#!/usr/bin/python3
"""
 Amenity class tests module.
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class testAmenity(unittest.TestCase):
    """Amenity test class."""

    def test_amenity(self):
        """Testing instances. """
        a = Amenity()
        self.assertTrue(isinstance(a, Amenity))
