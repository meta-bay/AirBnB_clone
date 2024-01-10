#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
''' Unit test module '''


class TestBaseModel(unittest.TestCase):
    ''' test the base model module '''
    def setUp(self):
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        del self.model1
        del self.model2

    def test_ids(self):
        ''' test if the ids are not equal'''
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_time(self):
        ''' tests the datetime '''
        self.assertNotEqual(self.model1.created_at, self.model2.updated_at)


if __name__ == "__main__":
    unittest.main()
