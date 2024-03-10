#!/usr/bin/python3
"""
City class module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class - inherits from BaseModel

    Attributes:
        state_id(string) - id of the city's state
        name(string) - name of the city
    """
    state_id = ""
    name = ""
    def __init__(self, *args, **kwargs):
        """Initialize State instance"""
        super().__init__(*args, **kwargs)
