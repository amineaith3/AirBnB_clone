#!/usr/bin/python3
"""Defines the entry point of this command interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter
    """
    prompt = "(hbnb) "
    cl = {"BaseModel", "User", "Place", "State", "City", "Amenity", "Review"}

    def do_create(self, arg):
        """Creates a new instance of BaseModel and prints the id
        """
        words = arg.split()
        if len(words) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.cl:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance
        based on the class name
        """
        words = arg.split()
        if len(words) == 2:
            for i, v in enumerate(words):
                if i == 0:
                    if v not in HBNBCommand.cl:
                        print("** class doesn't exist **")
                        return
                elif i == 1:
                    key = f"{words[0]}.{words[1]}"
                    objs = storage.all()
                    if key in objs:
                        print(objs[key])
                        return
                    print("** no instance found **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif len(words) == 0:
            print("** class name missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        ar = arg.split()
        if len(ar) == 0 or (ar[0] in HBNBCommand.cl and len(ar) == 1):
            objs = storage.all()
            print([str(obj) for obj in objs.values()])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        ar = arg.split()

        if len(ar) == 0:
            print("** class name missing **")
        elif ar[0] not in HBNBCommand.cl:
            print("** class doesn't exist **")
        elif len(ar) != 2:
            print("** instance id missing **")
        else:
            key = f"{ar[0]}.{ar[1]}"
            obj = storage.all()

            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        ar = arg.split()
        objs = storage.all()
        if len(ar) >= 4:
            key = f"{ar[0]}.{ar[1]}"
            if key in objs:
                rep = ar[3].replace('"', '')
                setattr(objs[key], ar[2], rep)
                objs[key].save()
            else:
                print("** no instance found **")
        elif len(ar) == 0:
            print("** class name missing **")
        elif ar[0] not in HBNBCommand.cl:
            print("** class doesn't exist **")
        elif len(ar) == 1:
            print("** instance id missing **")
        elif f"{ar[0]}.{ar[1]}" not in objs:
            print("** no instance found **")
        elif len(ar) == 2:
            print("** attribute name missing **")
        elif len(ar) == 3:
            print("** value missing **")

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Executes nothing on empty line
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
