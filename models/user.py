#!/usr/bin/python3
"""
User Module
"""
from base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel

    Attributes:
        email(string): user email
        password(string): user password
        first_name(string): first name of the user
        last_name(string): last name of the user
    """
    def __init__(self):
        """Initializes a new User object"""
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
