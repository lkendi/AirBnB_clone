#!/usr/bin/python3
"""
Review class module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class - inherits from BaseModel

    Attributes:
        place_id(str): id of the place in review
        user_id(str): id of user giving the review
        text(str): text contained in the review
    """
    place_id = ""
    user_id = ""
    text = ""
