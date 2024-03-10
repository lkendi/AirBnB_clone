#!/usr/bin/python3
"""Unittest module for the console"""
from console import HBNBCommand
from io import StringIO
import sys
import unittest
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Class containing unittests for the console"""
    def test_prompt(self):
        """Tests the console prompt"""
        self.assertEqual(HBNBCommand.prompt, '(hbnb) ')

    # def test_help(self):
    #     with patch("sys.stdout", new=StringIO()) as sample_stdout:
    #         self.assertTrue(HBNBCommand.onecmd("help"))

    # def test_do_quit(self):
    #     """Test that do_quit exits the console"""
    #     with patch("sys.stdout", new=StringIO()) as sample_stdout:
    #         self.assertTrue(HBNBCommand.onecmd("quit"))

    # def test_quit_help(self):
    #     help_text = ""
    #     pass

    # def test_do_EOF(self):
    #     """Test that do_EOF exits the console"""
    #     with patch("sys.stdout", new=StringIO()) as sample_stdout:
    #         self.assertTrue(HBNBCommand.onecmd("EOF"))

    # def test_emptyline(self):
    #     with patch("sys.stdout", new=StringIO()) as sample_stdout:
    #         self.assertTrue(HBNBCommand.onecmd(""))

    # def test_do_create(self):
    #     pass

    # def test_do_show(self):
    #     pass

    # def test_do_update(self):
    #     pass

    # def test_do_destroy(self):
    #     pass

    # def test_all(self):
    #     pass
