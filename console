#!/usr/bin/python3
"""
    Console Module
"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.stdin.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    attr_types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.stdin.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax."""
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if '.' not in line or '(' not in line or ')' not in line:
            return line

        try:  # to parse line left to right
            pline = line[:]

            # to isolate <class name>
            _cls = pline[:pline.find('.')]

            # to isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parentheses contain arguments, then parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')

                # if arguments exist beyond _id
                pline = pline[2].strip()
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}' and type(eval(pline)) == dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.stdin.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates an instance of a class")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        class_name, obj_id = self.extract_args(args)

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not obj_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{obj_id}"
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        class_name, obj_id = self.extract_args(args)

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not obj_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{obj_id}"

        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            class_name = args.split(' ')[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, value in storage._FileStorage__objects.items():
                if key.split('.')[0] == class_name:
                    print_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                print_list.append(str(value))

        print(print_list)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = sum(1 for key in storage._FileStorage__objects.keys() if key.startswith(args + '.'))
        print(count)

    def help_count(self):
        """Help information for the count command"""
        print("Counts the number of instances of a class")
        print("[Usage]: count <className>\n")

    def do_update(self, args):
        """ Updates a certain object with new info """
        class_name, obj_id, att_name, att_val, kwargs = self.extract_args(args)

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not obj_id:
            print("** instance id missing **")
            return

        key = f"{class_name}.{obj_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        if kwargs:
            args = [item for sublist in kwargs.items() for item in sublist]
        else:
            args = [att_name, att_val]

        new_dict = storage.all()[key]

        for i in range(0, len(args), 2):
            att_name, att_val = args[i], args[i + 1]

            if not att_name:
                print("** attribute name missing **")
                return

            if not att_val:
                print("** value missing **")
                return

            if att_name in HBNBCommand.attr_types:
                att_val = HBNBCommand.attr_types[att_name](att_val)

            new_dict.__dict__.update({att_name: att_val})

        new_dict.save()

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

    @staticmethod
    def extract_args(args):
        """Extracts and returns class name, object id, attribute name, attribute value, and kwargs from args"""
        class_name, obj_id, att_name, att_val, kwargs = '', '', '', '', ''

        # isolate class from id/args, ex: (<class>, delim, <id/args>)
        args = args.partition(" ")

        if args[0]:
            class_name = args[0]
        else:
            return class_name, obj_id, att_name, att_val, kwargs

        if class_name not in HBNBCommand.classes:
            return class_name, obj_id, att_name, att_val, kwargs

        # isolate id from args
        args = args[2].partition(" ")

        if args[0]:
            obj_id = args[0]
        else:
            return class_name, obj_id, att_name, att_val, kwargs

        # generate key from class and id
        key = f"{class_name}.{obj_id}"

        # determine if key is present
        if key not in storage.all():
            return class_name, obj_id, att_name, att_val, kwargs

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) == dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]

            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        return class_name, obj_id, att_name, att_val, kwargs


if __name__ == "__main__":
    HBNBCommand().cmdloop()
