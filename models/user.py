#!/usr/bin/python3
"""
User Module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel

    Attributes:
        email(string): user email
        password(string): user password
        first_name(string): first name of the user
        last_name(string): last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
