#!/usr/bin/python3
"""base_model"""


import uuid
import datetime
from models import storage


class BaseModel():
    """
        defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
            Initializes a new instance of BaseModel.

            Args:
                args: unused
                kwargs: Dictionary representation of the instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if value in ["created_at", "updated_at"]:
                        style = "%Y-%m-%dT%H:%M:%S.%f"
                        value = datetime.strptime(value, style)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """
            Returns a string representation of BaseModel instance.
        """
        c_n = self.__class__.__name__
        return "[{}] ({}) {}".format(c_n, self.id, self.__dict__)

    def save(self):
        """
            Updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
            Returns a dictionary containing
            all keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
