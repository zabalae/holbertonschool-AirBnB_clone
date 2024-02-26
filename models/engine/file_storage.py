#!/usr/bin/python3
'''Creates a class that serializes instances to a JSON file
    and deserializes JSON file to instances
'''

import json
from os.path import isfile
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    '''Serializes instances to a JSON file and deserializes
        JSON file to instances
    '''
    __file_path = "file.json" # path to the JSON file
    __objects = {} # dictionary

    def all(self):
        '''Will return the dictionary "__objects" '''
        return self.__objects

    def new(self, obj):
        '''Will set in "__objects" the obj with key <obj class name>.id'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Serializes "__objects" to the JSON file (path: __file_path)'''
        
        serialized_obj = {} # Creates empty dictionary
        
        for key, obj in self.__objects.items(): # Fills dictionary with elements from '__objects'
            serialized_obj[key] = obj.to_dict()
        
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_obj, file)

    def reload(self):
        '''Deserializes the JSON file to "__objects" '''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_obj = json.load(file)
                for key, obj_dict in loaded_obj.items():
                    class_name, obj_id = key.split('.')
                    class_ = globals()[class_name]
                    obj = class_(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
