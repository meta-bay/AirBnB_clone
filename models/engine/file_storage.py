#!/usr/bin/python3
'''
    FileStorage module
'''
import json
import os


class FileStorage():
    ''' File storage class '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' creates object dictionary '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        the_objs_dict = {key: obj}
        self.__objects.update(the_objs_dict)

    def save(self):
        ''' to json '''
        with open(self.__file_path, "w") as file:
            obj_dict = {
                key: val.to_dict() for key, val in self.__objects.items()
            }
            json.dump(obj_dict, file)

    def reload(self):
        '''
            deserializes the JSON file to __objects
        '''
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(self.__file_path, 'r', encoding="utf-8") as file:
            obj_dict = json.load(file)
            FileStorage.__objects = {
                key: self.extract_class(val["__class__"])
                (**val) for key, val in obj_dict.items()
            }

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
