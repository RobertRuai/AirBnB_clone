import unittest
import datetime
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""

    def setUp(self):
        """Set up for the test."""
        self.b1 = BaseModel()

    def tearDown(self):
        """Tear down the test."""
        storage.delete(self.b1)
        storage.reload()

    def test_id(self):
        """Test the id attribute."""
        self.assertTrue(hasattr(self.b1, "id"))
        self.assertIsInstance(self.b1.id, str)

    def test_created_at(self):
        """Test the created_at attribute."""
        self.assertTrue(hasattr(self.b1, "created_at"))
        self.assertIsInstance(self.b1.created_at, datetime)

    def test_updated_at(self):
        """Test the updated_at attribute."""
        self.assertTrue(hasattr(self.b1, "updated_at"))
        self.assertIsInstance(self.b1.updated_at, datetime)

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.b1.updated_at
        with patch('sys.stdout', new=StringIO()) as f:
            self.b1.save()
        new_updated_at = self.b1.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertIn(self.b1, storage.all().values())

    def test_to_dict(self):
        """Test the to_dict method."""
        b_dict = self.b1.to_dict()
        self.assertIsInstance(b_dict, dict)
        self.assertIn("__class__", b_dict)
        self.assertIn("id", b_dict)
        self.assertIn("created_at", b_dict)
        self.assertIn("updated_at", b_dict)
        self.assertEqual(b_dict["__class__"], "BaseModel")
        self.assertEqual(b_dict["id"], self.b1.id)
        self.assertEqual(b_dict["created_at"], self.b1.created_at.isoformat())
        self.assertEqual(b_dict["updated_at"], self.b1.updated_at.isoformat())

    def test_kwargs(self):
        """Test the kwargs functionality."""
        kwargs = {"id": "123", "created_at": "2021-01-01T01:00:00.000000",
                  "updated_at": "2021-01-01T02:00:00.000000", "name": "test"}
        b2 = BaseModel(**kwargs)
        self.assertEqual(b2.id, "123")
        self.assertEqual(b2.created_at, datetime(2021, 1, 1, 1, 0))
        self.assertEqual(b2.updated_at, datetime(2021, 1, 1, 2, 0))
        self.assertEqual(b2.name, "test")
