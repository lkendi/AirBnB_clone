#!/usr/bin/python3
"""program Module
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command - exits the program"""
        return True

    def do_EOF(self, args):
        """EOF - exists the program"""
        print()
        return True

    def emptyargs(self):
        """Handles empty args + ENTER"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it to JSON
        file and prints the id"""
        # TODO: Add code
        pass

    def do_show(self, args):
        """Prints the string representation of an inatance based on
        the classname and id"""
        # TODO: Add code
        pass

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        # TODO: Add code
        pass

    def do_all(self, args):
        """Prints a string representation of all instances based
        or not on the class name"""
        # TODO: Add code
        pass

    def do_update(self, args):
        """ Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)"""
        # TODO: Add code
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
