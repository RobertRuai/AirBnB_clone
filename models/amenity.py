#!/usr/bin/python3
"""Amenity module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity Class """

    name = ""

    def __init__(self, *args, **kwargs):
        """init function"""
        super().__init__(*args, **kwargs)
