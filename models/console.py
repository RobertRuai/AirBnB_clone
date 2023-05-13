#!/usr/bin/env python3
import cmd
from base_model import BaseModel
from models import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    intro = "Welcome to the HBNB command prompt. Type help or ? to list commands.\n"

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
        """Create a new instance of BaseModel and save it to the JSON file"""
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
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        
        obj_dict = FileStorage.all(cls)
        obj_id = args[1]
        key = "{}.{}".format(cls.__name__, obj_id)
        
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in FileStorage.all():
                print("** no instance found **")
            else:
                del FileStorage.all()[key]
                FileStorage.save()
    
    def do_all(self, arg):
        """Prints all string representations of all instances based or not on the class name"""
        objects = FileStorage.all()
        if not arg:
            print([str(objects[obj]) for obj in objects])
        elif arg not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            print([str(objects[obj]) for obj in objects if arg in obj])
    
    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in FileStorage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            setattr(FileStorage.all()[key], args[2], args[3])
            FileStorage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
