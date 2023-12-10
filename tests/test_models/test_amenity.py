#!/usr/bin/python3
"""tests for class amenity"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """tests for class amenity"""

    @classmethod
    def setUpClass(cls):
        """creates class instances"""
        cls.amenity = Amenity()
        cls.amenity.name = "Dinner"

    @classmethod
    def teardown(cls):
        """deletes class instances"""
        del cls.amenity

    def tearDown(self):
        """alternative deletion"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_amenity_attrs(self):
        """tests the attrs in amenity"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_typeof_attrs(self):
        """tests typeof attrs"""
        self.assertEqual(type(self.amenity.name), str)

    def test_issubclass(self):
        """tests if amenity is subclass of basemodel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_save_method(self):
        """tests save method"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_dict_method(self):
        """tests dict method"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
