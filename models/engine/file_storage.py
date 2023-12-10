#!/usr/bin/python3
"""Creating the class that sores the model"""
from os import path
import json


class FileStorage:
    """manages storage of airbnb in json format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionaty '__objects'"""
        return self.__objects

    def new(self, obj):
        """adds a new obj to the storage"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves the storage dict to a file"""
        the_dict = {}
        for key, value in self.__objects.items():
            the_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(the_dict))

    def reload(self):
        """loads saved dict from file"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.state import State
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                for value in json.loads(file.read()).values():
                    eval(value["__class__"])(**value)
