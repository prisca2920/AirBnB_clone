#!/usr/bin/python3
"""tests for FileStorage class"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """sets up the class"""
        cls.storage = FileStorage()
        try:
            os.rename(FileStorage._FileStorage__file_path, "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """deletes the class instance"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
            os.rename("test_file.json", FileStorage._FileStorage__file_path)
        except Exception:
            pass

    def test_all(self):
        """Test for the all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test for the new method"""
        model = BaseModel()
        self.storage.new(model)
        key = model.__class__.__name__ + "." + model.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test for the save method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        """Test for reload method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = model.__class__.__name__ + "." + model.id
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
