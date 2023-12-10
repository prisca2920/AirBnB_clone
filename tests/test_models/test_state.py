#!/usr/bin/python3
"""creates tests for class state"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """testing class state"""

    @classmethod
    def setUpClass(cls):
        """initializes instances of class"""
        cls.state = State()
        cls.state.name = "Michigan"

    @classmethod
    def teardown(cls):
        """deletes class state"""
        del cls.state

    def tearDown(self):
        """alternative deletion"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_state_attrs(self):
        """tests attrs of state"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_typeof_attrs(self):
        """tests type of attrs"""
        self.assertEqual(type(self.state.name), str)

    def test_is_subclass(self):
        """test if its a subclass"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_dict_method(self):
        """tests dict method"""
        self.assertEqual('to_dict' in dir(self.state), True)

    def test_save_method(self):
        """tests save method"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)


if __name__ == "__main__":
    unittest.main()
