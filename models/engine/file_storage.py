#!/usr/bin/python3
'''Creates a class that serializes instances to a JSON file
    and deserializes JSON file to instances
'''

import json
from os.path import isfile


class FileStorage:
    '''Serializes instances to a JSON file and deserializes
        JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Will return the dictionary "__objects" '''
        return self.__objects

    def new(self, obj):
        '''Will set in "__objects" the obj with key <obj class name>.id'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Serializes "__objects" to the JSON file (path: __file_path)'''
        serialized_obj = {}
        for key, value in self.__objects.items():
            serialized_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_obj, file)

    def reload(self):
        '''Deserializes the JSON file to "__objects" '''
        if isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_obj = json.load(file)
                for key, value in loaded_obj.items():
                    class_name, obj_id = key.split('.')

                    cls = globals()[class_name]
                    obj_instance = clas(**value)
                    self.__objects[key] = obj_instance
