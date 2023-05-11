#!/usr/bin/python3
"""Basemodel Module"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """initialises instance attribute values"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns  string representation"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """changes the updated_at time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary rep of all attrs"""
        n_dict = self.__dict__.copy()

        n_dict["created_at"] = self.created_at.isoformat()
        n_dict["updated_at"] = self.updated_at.isoformat()
        n_dict["__class__"] = self.__class__.__name__

        return n_dict
