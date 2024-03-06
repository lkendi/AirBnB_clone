#!/usr/bin/python3
"""Unittest modue for BaseModel class
"""


import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseMDel(unittest.TestCase):
    def test_init(self):
        # tests the creation of a new instance
        # with all arguments correctly set
        # default values of current date and time
        pass

    def test_init_custom_times(self):
        # custom time for created_at and/or
        # updated_at
        pass

    def test_init_wrong_data_types(self):
        # created_at and updated_at passed to
        # the function as non-datetime arguments
        pass

    def test_unique_id_assignment(self):
        # tests that each instance has a unique id
        pass

    def test_str_method(self):
        # tests the str method
        pass

    def test_save_method(self):
        # tests the save method
        pass

    def test_to_dict_method(self):
        #tests the to_dict method
        pass


    # might include empty strings,
    # wrong data types and None
    # values where necessary

if __name__ == "__main__":
    unittest.main()
