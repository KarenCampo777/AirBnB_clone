#!/usr/bin/python3
"""
Console module.

Entry point of the command interpreter
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
import re


classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):

    """
    HBNB Command prompt - console
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit this application
        """
        return True

    def do_EOF(self, arg):
        """
        Exit with EOF (end of file)
        """
        return True

    def emptyline(self):
        """
        Overwritte for not doing anything on empty line
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel.
        Saves it (to the JSON file)
        Prints the id of the new instance

        Usage: create <class name>

        """
        if not arg:
            print("** class name missing **")
        elif arg not in classes.keys():
            print("** class doesn't exist **")
        else:
            obj = classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints a string representation of an instance based on
        the class name and id.

        Usage: show <class name> <id>

        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            msg = "{}.{}".format(arg.split()[0], arg.split()[1])
            objs = storage.all()

            if msg not in objs:
                print("** no instance found **")
            else:
                print(objs[msg])

    def do_destroy(self, arg):
        """
        Destroy an instance based on the class name and id.

        Usage: destroy <class name> <id>

        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            msg = "{}.{}".format(arg.split()[0], arg.split()[1])
            objs = storage.all()

            if msg not in objs:
                print("** no instance found **")
            else:
                del(objs[msg])
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name

        Usage: all                - prints all instances
               all <class name>   - prints all instances of a given class

        """
        objs = storage.all()

        if not arg:
            my_list = [str(objs[key]) for key in objs]
            print(my_list)

        elif arg.split()[0] not in classes.keys():
            print("** class doesn't exist **")

        else:
            m = arg.split()[0]
            my_list = [str(objs[k]) for k in objs if k.split('.')[0] == m]
            print(my_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            msg = "{}.{}".format(arg.split()[0], arg.split()[1])
            objs = storage.all()

            if msg not in objs:
                print("** no instance found **")
            else:
                if len(arg.split()) < 3:
                    print("** attribute name missing **")
                elif len(arg.split()) < 4:
                    print("** value missing **")
                else:
                    if arg.split()[3].isdecimal():
                        setattr(objs[msg], arg.split()[2], int(arg.split()[3]))
                    else:
                        try:
                            val = float(arg.split()[3])
                            setattr(objs[msg], arg.split()[2], val)
                        except ValueError:
                            val = re.split("( |\\\".*?\\\"|'.*?')", arg)
                            val = [w for w in val if w.strip()]
                            val = val[3].strip('"')
                            setattr(objs[msg], arg.split()[2], val)
                    objs[msg].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
