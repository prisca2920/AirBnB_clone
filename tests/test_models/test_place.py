#!/usr/bin/python3
"""tests class place"""
import unittest
import os
from os import getenv
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """tests class place"""

    @classmethod
    def setUpClass(cls):
        """creates class instances"""
        cls.place = Place()
        cls.place.city_id = "9876-abcd"
        cls.place.user_id = "4321-xyza"
        cls.place.name = "calibri"
        cls.place.description = "amazing stay"
        cls.place.number_rooms = 98
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 50000
        cls.place.price_by_night = 67
        cls.place.latitude = 56.0
        cls.place.longitude = 57.0
        cls.place.amenity_ids = ["7642-lksdjkl"]

    @classmethod
    def teardown(cls):
        """deletes class intances"""
        del cls.place

    def tearDown(self):
        """alternative deletion"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_place_attrs(self):
        """tests place attrs"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_typeof_attr(self):
        """tests attr types"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_issubclass(self):
        """tests if subclass of basemodel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_method(self):
        """tests save method"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_dict_method(self):
        """tests dict method"""
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
