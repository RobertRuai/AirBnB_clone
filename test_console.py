import unittest
from unittest.mock import patch
from io import StringIO
from models.console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """Test the HBNB console."""

    def setUp(self):
        """Set up for the test."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down the test."""
        self.console.do_destroy("BaseModel " + str(self.b1.id))
        self.console.do_destroy("User " + str(self.u1.id))
        storage.reload()

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
        b_id = f.getvalue().strip()
        self.assertTrue(len(b_id) > 0)
        b1 = storage.all()["BaseModel." + b_id]
        self.assertIsNotNone(b1)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
        u_id = f.getvalue().strip()
        self.assertTrue(len(u_id) > 0)
        u1 = storage.all()["User." + u_id]
        self.assertIsNotNone(u1)

    def test_show(self):
        """Test show command."""
        self.b1 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(self.b1.id))
        self.assertIn(str(self.b1.id), f.getvalue())

        self.u1 = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User {}".format(self.u1.id))
        self.assertIn(str(self.u1.id), f.getvalue())

    def test_all(self):
        """Test all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
        self.assertIn("BaseModel", f.getvalue())
        self.assertIn("User", f.getvalue())

        b1 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
        self.assertIn(str(b1.id), f.getvalue())

        u1 = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
        self.assertIn(str(u1.id), f.getvalue())

    def test_destroy(self):
        """Test destroy command."""
        self.b1 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel {}".format(self.b1.id))
        self.assertEqual(f.getvalue().strip(), "")

        self.u1 = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User {}".format(self.u1.id))
        self.assertEqual(f.getvalue().strip(), "")

    def test_update(self):
        """Test update command."""
        self.b1 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel {} name 'test'".format(self.b1.id))
        self.assertEqual(f.getvalue().strip(), "")
        self.assertEqual(self.b1.name, "test")

        self.u1 = User()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User {} age 30".format(self.u1.id))
        self.assertEqual(f.getvalue().strip(), "")
        self.assertEqual(self.u1.age)
