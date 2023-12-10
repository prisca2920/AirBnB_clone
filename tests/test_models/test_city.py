#!/usr/bin/python3
"""tests for class city"""
import unittest
import os
from os import getenv
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """tests for class city"""

    @classmethod
    def setUpClass(cls):
        """creating city instances"""
        cls.city = City()
        cls.city.name = "nairobi"
        cls.city.state_id = "NA"

    @classmethod
    def teardown(cls):
        """deletes class instance"""
        del cls.city

    def tearDown(self):
        """alternative deletion"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_city_attrs(self):
        """tests attrs of city"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_typeof_attrs(self):
        """tests attrs of city"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_issubclass(self):
        """tests if city is subclass of basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_method(self):
        """tests save method"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_dict_method(self):
        """tests dict method"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
