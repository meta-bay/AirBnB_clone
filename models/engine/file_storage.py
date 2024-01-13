#!/usr/bin/python3
import json
import os
'''
    File storage module
'''


class FileStorage():
    '''
    serializes instances to a JSON file and 
    deserializes JSON file to instances
    '''
    __file_path = 'file.json'
    __objects = {}
    def all(self):
        ''' returns the dictionary __objects '''
        return type(self).__objects

    def new(self, obj):
        ''' sets __objects the obj with
            key <obj class name>.id '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''
            serializes __objects to the JSON file
        '''
        with open(self.__file_path, "w") as file:
            obj_to_dict = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        '''
            deserializes the JSON file to __objects
        '''
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(self.__file_path, 'r', encoding="utf-8") as file:
            obj_dict = json.load(file)
            FileStorage.__objects = {key: self.extract_class(val["__class__"])(**val) for key, val in obj_dict.items()}

    def extract_class(self, name=None):
        ''' extracts the class from the dictionary'''
        from models.base_model import BaseModel

        if not name:
            return
        classes = {
            "BaseModel": BaseModel
        }
        try:
            return classes[name]
        except Exception:
            pass