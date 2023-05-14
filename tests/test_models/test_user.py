#!/usr/bin/python3
"""User class test module"""
import unittest
from models.user import User
from models.base_model import BaseModel


class testUser(unittest.TestCase):
    """User test class."""

    def test_user(self):
        """Testing instances"""
        a = Usere()
        self.assertTrue(isinstance(a, User))
