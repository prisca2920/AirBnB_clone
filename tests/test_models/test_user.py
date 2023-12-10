#!/usr/bin/python3
"""creating tests for user"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """testing class user"""

    @classmethod
    def setUpClass(cls):
        """sets up the class"""
        cls.user = User()
        cls.user.first_name = "ann"
        cls.user.last_name = "mwangi"
        cls.user.email = "annmwangi@gmail.com"
        cls.user.password = "mwangiann"

    @classmethod
    def teardown(cls):
        """deletes the setup class"""
        del cls.user

    def tearDown(self):
        """tries another method of deleting"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_users_attr(self):
        """if the attr are correct"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_typeof_attr(self):
        """tests type of attr for user"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save_User(self):
        """tests whether saves work"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_dict_method(self):
        """tests if dict method works"""
        self.assertEqual('to_dict' in dir(self.user), True)

    def test_is_subclass(self):
        """tests whether its a subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()
