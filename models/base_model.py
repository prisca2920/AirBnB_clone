#!/usr/bin/python3
"""creating the base class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """creating an empty class base"""
    def __init__(self, *args, **kwargs):
        """initializing the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            dformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, dformat))
                elif key != "__class__":
                    setattr(self, key, value)
        storage.new(self)

    def __str__(self):
        """returns the str representation"""
        class_name = self.__class__.__name__
        return f"[{class name}] ({self.id}) {self.__dict__}"

    def save(self):
        """updated the current time"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dict representation"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
