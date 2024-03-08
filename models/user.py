#!/usr/bin/python3
from base_model import BaseModel

class User(BaseModel):
    """
    A class User that inherits from BaseModel

    Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string 
    """
    def __init__(self):
        super().__init__()
        self.email = "" 
        self.password = "" 
        self.first_name = ""
        self.last_name = ""
