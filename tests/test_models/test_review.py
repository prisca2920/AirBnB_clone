#!/usr/bin/python3
"""tets for class review"""
import unittest
import os
from os import getenv
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """tests for class review"""

    @classmethod
    def setUpClass(cls):
        """set up instances of review"""
        cls.rev = Review()
        cls.rev.place_id = "1245-gfsd"
        cls.rev.user_id = "123-xyz"
        cls.rev.text = "The best stay ever"

    @classmethod
    def teardown(cls):
        """deletes the class review"""
        del cls.rev

    def tearDown(self):
        """alternative delete method"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_review_attrs(self):
        """tests attrs of class review"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_typeof_attrs(self):
        """tests typeof attrs"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    def test_issubclass(self):
        """tests if its a subclass of basemodel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Review(self):
        """tests save method"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_dict_method(self):
        """tests dict method"""
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
