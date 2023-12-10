#!/usr/bin/python3
"""creates a class user from base"""
from models.base_model import BaseModel


class User(BaseModel):
    """creates a class user"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
