#!/usr/bin/env python3
"""Console Module"""

import cmd
from base_model import BaseModel
from models import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in FileStorage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in FileStorage.all().keys():
            print("** no instance found **")
            return
        print(FileStorage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id 
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in FileStorage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in FileStorage.all().keys():
            print("** no instance found **")
            return
        del FileStorage.all()[key]
        FileStorage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on
        the class name.
        """
        args = arg.split()
        if len(args) == 0:
            obj_list = [str(obj) for obj in FileStorage.all().values()]
            print(obj_list)
        elif args[0] not in FileStorage.classes.keys():
            print("** class doesn't exist **")
            return
        else:
            obj_list = [str(obj) for obj in FileStorage.all().values()
                        if type(obj).__name__ == args[0]]
            print(obj_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating
        attribute (save the change into the JSON file).
        
        """
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if len(args_list) < 2:
            print("** class name missing **")
            return
        class_name = args_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args_list) < 3:
            print("** instance id missing **")
            return
        obj_id = args_list[1]
        obj = FileStorage.get(class_name, obj_id)
        if not obj:
            print("** no instance found **")
            return
        if len(args_list) < 4:
            print("** attribute name missing **")
            return
        attr_name = args_list[2]
        if len(args_list) < 5:
            print("** value missing **")
            return
        attr_value_str = args_list[3]
        if len(args_list) > 5:
            print("** value missing **")
            return
        if hasattr(obj, attr_name):
            attr_value_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_value_type(attr_value_str)
            except ValueError:
                attr_value = attr_value_str
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** no instance found **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
