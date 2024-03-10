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

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help quit")

    def test_help_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help EOF")

    def test_help_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help create")

    def test_help_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help destroy")

    def test_help_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help all")

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")

    def test_help_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help update")

    def test_help_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help help")

    def test_do_quit(self):
        self.assertTrue(self.console.do_quit(None))

    def test_do_EOF(self):
        """Test that do_EOF exits the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.do_EOF(None))
            self.assertEqual(f.getvalue(), '\n')

    def test_emptyline(self):
        self.assertIsNone(self.console.emptyline())

    def test_do_create_classname_missing(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create('')
            self.assertEqual(f.getvalue()
                             .strip(), "** class name missing **")

    def test_do_create_invalid_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create('MyClass')
            self.assertEqual(f.getvalue()
                             .strip(), "** class doesn't exist **")

    def test_do_create_basemodel_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create('BaseModel')
            output = f.getvalue().strip()
            self.assertNotEqual(output, "** class name missing **")
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_do_destroy_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy('')
            self.assertEqual(f.getvalue()
                             .strip(), "** class name missing **")

    def test_do_destroy_invalid_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy('MyClass')
            self.assertEqual(f.getvalue()
                             .strip(), "** class doesn't exist **")

    def test_do_destroy_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy('BaseModel')
            self.assertEqual(f.getvalue()
                             .strip(), "** instance id missing **")

    def test_do_destroy_instance_not_found(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy('BaseModel 123')
            self.assertEqual(f.getvalue()
                             .strip(), "** no instance found **")

    def test_do_all_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_all('MyClass')
            self.assertIn("** class doesn't exist **",
                          f.getvalue())

    def test_do_show_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show('')
            self.assertEqual(f.getvalue()
                             .strip(), "** class name missing **")

    def test_do_show_invalid_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show('MyClass')
            self.assertEqual(f.getvalue()
                             .strip(), "** class doesn't exist **")

    def test_do_show_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show('BaseModel')
            self.assertEqual(f.getvalue()
                             .strip(), "** instance id missing **")

    def test_do_update_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_update('')
            self.assertEqual(f.getvalue()
                             .strip(), "** class name missing **")

    def test_do_update_invalid_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_update('MyClass')
            self.assertEqual(f.getvalue().
                             strip(), "** class doesn't exist **")

    def test_do_update_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_update('BaseModel')
            self.assertEqual(f.getvalue().
                             strip(), "** instance id missing **")

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")


if __name__ == "__main__":
    unittest.main()
