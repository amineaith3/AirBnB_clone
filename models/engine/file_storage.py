#!/usr/bin/python3
"""This modules defines a FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class manages data storage and updates.

    It serializes and deserializes instances to JSON
    and vice versa.

    Attributes:
        __file_path (str): The JSON file.
        __objects (dict): Dictionary to store objects based on
                          their id.
    """

    def __init__(self):
        """Initializes object."""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns __objects."""
        return self.__objects

    def new(self, obj):
        """Adds <obj class name>.id to __objects."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Converts __objects to JSON file."""
        data = {}

        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """Converts JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)

                for item in data.values():
                    cls_name = item["__class__"]
                    del item["__class__"]
                    self.new(eval(cls_name)(**item))
        except FileNotFoundError:
            return
