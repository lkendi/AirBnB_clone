#!/usr/bin/python3
"""
State class module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class - inherits from BaseModel

    Attributes:
        name(string) - name of the state"""
    name = ""
    def __init__(self, *args, **kwargs):
        """Initialize State instance"""
        super().__init__(*args, **kwargs)
