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

    def new(self, obj):
        '''Will set in "__objects" the obj with key <obj class name>.id'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
        # self.__objects[key] = obj

    def all(self):
        '''Will return the dictionary "__objects" '''
        return FileStorage.__objects
        # return self.__objects
    
    # def get_all(self, cls):
    #    '''Returns a dictionary of all instances of the given class'''
    #    all_instances = {}
    #    for key, obj in self.__objects.items():
    #        if type(obj) == cls:
    #            all_instances[key] = obj
    #    return all_instances
    
    def save(self):
        '''Serializes "__objects" to the JSON file (path: __file_path)'''

        all_objs = FileStorage.__objects
        serialized_obj = {}

        for obj in all_objs.keys():
            serialized_obj[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_obj, file)
        # serialized_obj = {}   # Creates empty dictionary

        # for key, obj in self.__objects.items():
        #    serialized_obj[key] = obj.to_dict()

        # with open(self.__file_path, 'w', encoding='utf-8') as file:
        #    json.dump(serialized_obj, file)

    def reload(self):
        '''Deserializes the JSON file to "__objects" '''
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                try:
                    serialized_obj = json.load(file)
                    for key, value in serialized_obj.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

        # try:
        #    with open(self.__file_path, 'r', encoding='utf-8') as file:
        #        loaded_obj = json.load(file)
        #        for key, obj_dict in loaded_obj.items():
        #            class_name, obj_id = key.split('.')
        #            class_ = globals()[class_name]
        #            obj = class_(**obj_dict)
        #            self.__objects[key] = obj
        # except FileNotFoundError:
        #    pass