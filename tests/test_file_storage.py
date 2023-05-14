import os
import json
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test all() method"""
        # Create a few instances
        b1 = BaseModel()
        b2 = BaseModel()
        u1 = User()
        u2 = User()

        # Add instances to storage
        self.storage.new(b1)
        self.storage.new(b2)
        self.storage.new(u1)
        self.storage.new(u2)
        self.storage.save()

        # Ensure that all() returns a dictionary
        self.assertIsInstance(self.storage.all(), dict)

        # Ensure that all objects are in dictionary
        objects = self.storage.all()
        self.assertIn(b1, objects.values())
        self.assertIn(b2, objects.values())
        self.assertIn(u1, objects.values())
        self.assertIn(u2, objects.values())

    def test_new(self):
        """Test new() method"""
        # Create an instance
        b1 = BaseModel()

        # Add instance to storage
        self.storage.new(b1)
        self.storage.save()

        # Ensure that instance is in dictionary
        objects = self.storage.all()
        self.assertIn(b1, objects.values())

    def test_save(self):
        """Test save() method"""
        # Create an instance
        b1 = BaseModel()

        # Add instance to storage and save
        self.storage.new(b1)
        self.storage.save()

        # Ensure that file was created
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

        # Ensure that file was properly saved
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
            self.assertIn(b1.id, data.keys())

    def test_reload(self):
        """Test reload() method"""
        # Create an instance
        b1 = BaseModel()

        # Add instance to storage and save
        self.storage.new(b1)
        self.storage.save()

        # Clear objects in memory
        FileStorage._FileStorage__objects = {}

        # Reload objects from file
        self.storage.reload()

        # Ensure that instance is in dictionary
        objects = self.storage.all()
        self.assertIn(b1, objects.values())
