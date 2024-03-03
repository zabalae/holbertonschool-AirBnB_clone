#!/usr/bin/python3
'''Creates a class that serializes instances to a JSON file
    and deserializes JSON file to instances
'''

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    '''Serializes instances to a JSON file and deserializes
        JSON file to instances
    '''
    __file_path = "file.json"   # path to the JSON file
    __objects = {}   # dictionary
    classes = {'BaseModel': BaseModel, 'User': User,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Place': Place, 'Review': Review}

    def new(self, obj):
        '''Will set in "__objects" the obj with key <obj class name>.id'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
        # self.__objects[key] = obj

    def all(self):
        '''Will return the dictionary "__objects" '''
        return FileStorage.__objects
    
    def save(self):
        '''Serializes "__objects" to the JSON file (path: __file_path)'''

        all_objs = FileStorage.__objects
        serialized_obj = {}

        for obj in all_objs.keys():
            serialized_obj[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_obj, file)

    def reload(self):
        '''Deserializes the JSON file to "__objects" '''
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file_path:
            objs = json.load(file_path)
            FileStorage.__objects = {}
            for key in objs:
                name = key.split(".")[0]
                FileStorage.__objects[key] = FileStorage.classes[name](**objs[key]) 
