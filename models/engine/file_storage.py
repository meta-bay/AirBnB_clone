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
    __file_path = 'storage.json'
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
            file.write(json.dumps(obj_to_dict))

    def reload(self):
        '''
            deserializes the JSON file to __objects
        '''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.loads(file.read())
                type(self).__objects = {key: value["__class__"] for key, value in obj_dict.items()}

