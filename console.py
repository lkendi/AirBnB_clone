#!/usr/bin/python3
"""program Module
"""

import cmd
from models.base_model import BaseModel
from models import storage


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

    # def do_create(self, args):
    #     """Creates a new instance of BaseModel, saves it to JSON
    #     file and prints the id"""
    #     if not args:
    #         print("** class name missing **")
    #     else:
    #         class_name = args.split()[0]
    #         if class_name not in ["BaseModel"]:
    #             print("** class doesn't exist **")
    #         else:
    #             new = eval(class_name)()
    #             new.save()
    #             print(new.id)

    # def do_show(self, args):
    #     """Prints the string representation of an instance based on
    #     the classname and id"""
    #     if not args:
    #         print("** class name missing **")
    #     line = args.split()
    #     if line[0] not in ["BaseModel"]:
    #         print("** class doesn't exist **")
    #         return
    #     if len(line) < 2:
    #         print("** instance id missing **")
    #         return
    #     id = line[1]
    #     objects = storage.all()
    #     key = "BaseModel" + id
    #     if key in objects:
    #         print(objects[key])
    #     else:
    #         print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if not args:
            print("** class name missing **")
        # TODO: Complete this function

    def do_all(self, args):
        """Prints a string representation of all instances based
        or not on the class name"""
        # TODO: Add code
        pass

    def do_update(self, args):
        """ Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)"""
        if not args:
            print("** class name missing **")
        # TODO: Complete this code
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
