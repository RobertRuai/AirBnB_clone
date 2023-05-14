#!/usr/bin/env python3
import cmd
import shlex
import ast
from models.base_model import BaseModel
from models import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    intro = "Welcome to the HBNB command prompt.\n"
    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City, 'State': State, 'Amenity': Amenity,
               'Review': Review}

    def do_quit(self, arg):
        """ Exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF to exit the program (Ctrl-D) """
        print()
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything """
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel,saves it to JSON file"""
        if not arg:
            print("** class name missing **")
            return

        try:
            cls = eval(arg)
            obj = cls()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")
            
    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        class_name = args[0]
        obj_id = args[1]
        instances = FileStorage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key not in instances:
            print("** no instance found **")
            return
        obj = instances[key]
        print(obj)
    
    def do_count(self, arg):
        """ Counts the number of instances of a class """
        class_name = arg.split('.')[0]
        if class_name not in self.classes:
            print("** class doesn't exist")
        else:
            count = self.classes[class_name].count()
            print(count)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        class_name = args[0]
        obj_id = args[1]
        instances = FileStorage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key not in instances:
            print("** no instance found **")
            return
        del instances[key]
        FileStorage.save()

    def do_all(self, arg):
        """
        Prints all string repr of all instances based or not on the class name
        """
        if not arg:
            instances = FileStorage.all().values()
            print([str(instance) for instance in instances])
        else:
            class_name = arg.split('.')[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
            else:
                instances = self.classes[class_name].all()
                print([str(instance) for instance in instances])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attributes using a dictionary
        """
        args = arg.split()
        if len(args) < 3:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        class_name = args[0]
        obj_id = args[1]
        instances = FileStorage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key not in instances:
            print("** no instance found **")
            return
        obj = instances[key]
        try:
            dict_str = shlex.split(args[2])
            if len(dict_str) == 0 or "{" not in dict_str[0]:
                raise ValueError
            update_dict = ast.literal_eval(dict_str[0])
            if not isinstance(update_dict, dict):
                raise ValueError
        except (ValueError, SyntaxError):
            print("** invalid dictionary argument **")
            return
        for k, v in update_dict.items():
            setattr(obj, k, v)
        FileStorage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
