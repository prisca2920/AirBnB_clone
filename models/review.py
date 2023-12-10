#!/usr/bin/python3
"""creates class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """initializes class review"""
    place_id = ''
    user_id = ''
    text = ''
