#!/usr/bin/python3
"""Console Module
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter class"""
    prompt = "(hbnb) "
    list_of_classes = ["BaseModel", "User", "Amenity",
                       "Place", "Review", "State", "City"]

    def do_quit(self, args):
        """Quit command - exits the program"""
        return True

    def do_EOF(self, args):
        """EOF - exists the program"""
        print()
        return True

    def emptyline(self):
        """Handles empty line + ENTER"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it to JSON
        file and prints the id"""
        if not args:
            print("** class name missing **")
            return
        elif args not in self.list_of_classes:
            print("** class doesn't exist **")
        else:
            new = eval(args)()
            new.save()
            print(new.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on
        the classname and id"""
        if not args:
            print("** class name missing **")
            return
        line = args.split()
        if line[0] not in self.list_of_classes:
            print("** class doesn't exist **")
            return
        elif len(line) < 2:
            print("** instance id missing **")
            return
        else:
            objects = storage.all()
            key = f"{line[0]}.{line[1]}"
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if not args:
            print("** class name missing **")
            return
        line = args.split()
        if line[0] not in self.list_of_classes:
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        key = f"{line[0]}.{line[1]}"
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        else:
            del objs[key]
            storage.save()

    def do_all(self, args):
        """Prints a string representation of all instances based
        or not on the class name"""
        objs = storage.all()
        if not args:
            print(str[v] for v in objs.values())
        elif args not in self.list_of_classes:
            print("** class doesn't exist **")
        else:
            for k, v in objs.items():
                if k.startswith(args):
                    print(str(v))

    def do_update(self, args):
        """ Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)"""
        if not args:
            print("** class name missing **")
            return
        line = args.split()
        if line[0] not in self.list_of_classes:
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = f"{line[0]}.{line[1]}"
        if key not in objs:
            print("** no instance found **")
            return
        elif len(line) < 3:
            print("** attribute name missing **")
            return
        elif len(line) < 4:
            print("** value missing **")
            return
        else:
            class_instance = objs[key]
            setattr(class_instance, line[2], line[3])
            class_instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
