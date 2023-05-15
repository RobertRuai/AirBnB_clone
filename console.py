#!/usr/bin/env python3
import cmd
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
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(args) > 1:
            class_name = args[0]
            obj_id = args[1]
            instances = FileStorage.all(self)
            key = "{}.{}".format(class_name, obj_id)
            if key not in instances:
                print("** no instance found **")
                return
            obj = instances[key]
            print(obj)
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        ags = arg.split()
        if len(ags) == 0:
            print("** class name missing **")
        elif ags[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(ags) > 1:
            value = "{}.{}".format(ags[0], ags[1])
            if value in FileStorage.all(self):
                FileStorage.all(self).pop(value)
                FileStorage.save(self)
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        """
        Prints all string repr of all instances
        based or not on the class name
        """
        if not arg:
            instances = FileStorage.all(self).values()
            print([str(instance) for instance in instances])
        else:
            class_name = arg.split('.')[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
            else:
                for key, value in FileStorage.all(self).items():
                    if arg in key:
                        print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attributes using a dictionary
        """
        ags = arg.split()
        if len(ags) == 0:
            print("** class name missing **")
        elif ags[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(ags) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(ags[0], ags[1])
            if key in FileStorage.all(self):
                if len(ags) > 2:
                    if len(ags) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                           FileStorage.all(self)[key],
                           ags[2],
                           ags[3][1:-1])
                        FileStorage.all(self)[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
