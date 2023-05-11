#!/usr/bin/python3
"""FileStorage module"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ serializes instances to JSON, deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            ob_key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[ob_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        n_string = {}
        for key, value in self.__objects.items():
            n_string[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(n_string, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if (os.path.isfile(self.__file_path)):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                n_obj = json.load(file)
                for key, value in n_obj.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
