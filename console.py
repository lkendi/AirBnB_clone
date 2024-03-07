#!/usr/bin/python3
"""program Module
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command - exits the program"""
        return True

    def do_EOF(self, line):
        """EOF - exists the program"""
        print()
        return True

    def emptyline(self):
        """Handles empty line + ENTER"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
