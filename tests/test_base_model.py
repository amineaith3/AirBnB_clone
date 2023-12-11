#!/usr/bin/python3
"""Defines a unittests for BaseModel class."""
from models.base_model import BaseModel
import os
import unittest


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.cls = BaseModel()

    @classmethod
    def tearDownClass(self):
        del self.cls

    def test_ClsInitialization(self):
        self.assertIsInstance(self.cls, BaseModel)
        self.assertTrue(hasattr(self.cls, 'id'))
        self.assertTrue(hasattr(self.cls, 'updated_at'))
        self.assertTrue(hasattr(self.cls, 'created_at'))


if __name__ == "__main__":
    unittest.main()
