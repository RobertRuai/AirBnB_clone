#!/usr/bin/python3
"""review class test module"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class testReview(unittest.TestCase):
    """review test class."""

    def test_review(self):
        """Testing instances"""
        a = Review
        self.assertTrue(issubclass(a, BaseModel))
