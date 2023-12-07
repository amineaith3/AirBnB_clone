#!/usr/bin/python3
"""file_storage"""


import json
import os.path


class FileStorage():
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    def __init__(self):
        """Inisializes a new instance of FileStorage"""
        self.__file_path = "database.json"
        self.__objects = dict()

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        for key, value in self.__objects.items():
            result[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as outfile:
            json.dump(result, outfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, 'r', encoding="UTF-8") as infile:
            data = json.load(infile)
        
