#!/usr/bin/python3
"""test_base_model"""


from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """test BaseModel class"""

    def test_class_type(self):
        """test the type of the instance atributes"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_(self):
        """test the __str__ method"""
        my_model = BaseModel()
        str_ = my_model.__str__()
        id = my_model.id
        dic = my_model.__dict__
        self.assertEqual(str_, "[BaseModel] ({}) {}".format(id, dic))

    def test_save(self):
        """test the save method"""
        my_model = BaseModel()
        created_at = my_model.created_at
        my_model.save()
        self.assertIs(my_model.created_at, created_at)
        self.assertIsNot(my_model.updated_at, my_model.created_at)

    def test_to_dict(self):
        """test the to_dict method"""
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        self.assertNotIsInstance(my_model.__str__(), dict)
        self.assertIsInstance(my_model_json, dict)
