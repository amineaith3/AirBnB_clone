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
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return #kemlt had reload
