#!/usr/bin/python3
"""test for BaseModel"""
import unittest
import os
from os import getenv
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test cases for basemodel"""

    @classmethod
    def setUpClass(cls):
        """creates an instance of a class"""
        cls.base = BaseModel()
        cls.base.name = "mercy"
        cls.base.num = 10

    @classmethod
    def teardown(cls):
        """deletes the instance"""
        del cls.base

    def tearDown(self):
        """alternative deletion"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_BaseModel_attr(self):
        """tests attrs of basemodel"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_method(self):
        """tests the constructor of basemodel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_method(self):
        """tests the save method"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_dict_method(self):
        """tests the dict method"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
