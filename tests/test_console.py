#!/usr/bin/python3
"""Unittest module for the console"""
from console import HBNBCommand
from io import StringIO
import unittest
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Class containing unittests for the console"""
    def setUp(self):
        self.console = HBNBCommand()

    def test_prompt(self):
        self.assertEqual(HBNBCommand.prompt, '(hbnb) ')

    def test_do_quit(self):
        self.assertTrue(self.console.do_quit(None))

    def test_do_EOF(self):
        """Test that do_EOF exits the console"""
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.assertTrue(self.console.do_EOF(None))
            self.assertEqual(sample_stdout.getvalue(), '\n')

    def test_emptyline(self):
        self.assertIsNone(self.console.emptyline())

    def test_do_create_classname_missing(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_create('')
            self.assertEqual(sample_stdout.getvalue()
                             .strip(), "** class name missing **")

    def test_do_create_invalid_classname(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_create('MyClass')
            self.assertEqual(sample_stdout.getvalue()
                             .strip(), "** class doesn't exist **")

    def test_do_create_basemodel_class(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_create('BaseModel')
            output = sample_stdout.getvalue().strip()
            self.assertNotEqual(output, "** class name missing **")
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_do_destroy_missing_class_name(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_destroy('')
            self.assertEqual(sample_stdout.getvalue()
                             .strip(), "** class name missing **")

    def test_do_destroy_invalid_classname(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_destroy('MyClass')
            self.assertEqual(sample_stdout.getvalue()
                             .strip(), "** class doesn't exist **")

    def test_do_destroy_missing_instance_id(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_destroy('BaseModel')
            self.assertEqual(sample_stdout.getvalue()
                             .strip(), "** instance id missing **")

    def test_do_destroy_instance_not_found(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_destroy('BaseModel 123')
            self.assertEqual(sample_stdout.getvalue()
                             .strip(), "** no instance found **")

    def test_do_all_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_all('MyClass')
            self.assertIn("** class doesn't exist **",
                          sample_stdout.getvalue())

    def test_do_show_missing_class_name(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_show('')
            self.assertEqual(sample_stdout.getvalue()
                             .strip(), "** class name missing **")

    def test_do_show_invalid_classname(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_show('MyClass')
            self.assertEqual(sample_stdout.getvalue()
                             .strip(), "** class doesn't exist **")

    def test_do_show_missing_instance_id(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_show('BaseModel')
            self.assertEqual(sample_stdout.getvalue()
                             .strip(), "** instance id missing **")

    def test_do_update_missing_class_name(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_update('')
            self.assertEqual(sample_stdout.getvalue()
                             .strip(), "** class name missing **")

    def test_do_update_invalid_classname(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_update('MyClass')
            self.assertEqual(sample_stdout.getvalue().
                             strip(), "** class doesn't exist **")

    def test_do_update_missing_instance_id(self):
        with patch("sys.stdout", new=StringIO()) as sample_stdout:
            self.console.do_update('BaseModel')
            self.assertEqual(sample_stdout.getvalue().
                             strip(), "** instance id missing **")


if __name__ == "__main__":
    unittest.main()