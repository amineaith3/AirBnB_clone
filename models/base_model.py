#!/usr/bin/python3
"""base_model"""


import uuid
import datetime
import models


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
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.datetime.strptime(value, self.time) #strptime in datetime in datetime wa9ila
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

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
        models.storage.save()

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
