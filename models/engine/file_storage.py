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
        serialized_objects = dict()
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as outfile:
            json.dump(serialized_objects, outfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        condition1 = os.path.exists(self.__file_path)
        condition2 = os.path.getsize(self.__file_path) > 1
        if not (condition1 and condition2):
            return
        with open(self.__file_path, 'r', encoding="UTF-8") as infile:
            data = json.load(infile)
