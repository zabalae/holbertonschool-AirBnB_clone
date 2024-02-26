#!/usr/bin/python3
'''Contains the entry point of the command interpreter'''


import cmd
import json
import os
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    file_path = 'file.json'
    classes = {'BaseModel': BaseModel, 'User': User,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Place': Place, 'Review': Review}

    def do_quit(self, arg):
        '''Will exit the program'''
        return True

    def do_EOF(self, arg):
        '''Will exit the program'''
        print("")
        return True

    def do_help(self, arg):
        '''Will show help'''
        return super().do_help(arg)

    def emptyline(self):
        '''Do nothing when input is empty line'''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it
            (to the JSON file), and prints the id
        '''
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        '''Prints the string representation of an instance based on
            the class name and id
        '''
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in BaseModel.__objects:
                print(BaseModel.__objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id (save the
            change into the JSON file)
        '''
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in BaseModel.__objects:
                del BaseModel.__objects[key]
                BaseModel.save_to_file()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        '''Prints all str representation of all instances based or not
            on the class name
        '''
        args = shlex.split(arg)
        instances = []
        if len(args) == 0:
            for obj in BaseModel.__objects.values():
                instances.append(str(obj))
        elif args[0] not in self.classes:
            print("** class doesn't exits **")
            return
        else:
            for key, obj in BaseModel.__objects.items():
                if args[0] == key.split(".")[0]:
                    instances.append(str(obj))
        print(instances)

    def do_update(self, arg):
        '''Updates an instance based on the class name and id by adding
            or updating attribute
        '''
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in BaseModel.__objects:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = BaseModel.__objects[key]
                attribute_name = args[2]
                attribute_value = args[3]
                setattr(obj, attribute_name, attribute_value)
                obj.save()

    def precmd(self, line):
        '''Will execute before each command'''
        if '.' not in line:
            return line
        cmd, arg = line.split('.', 1)
        arg = arg.replace('(', ' ')
        arg = arg.replace(')', ' ')
        line = cmd + ' ' + arg
        return line

    def postcmd(self, stop, line):
        '''Will execute after each command'''
        BaseModel.save_to_file()
        return stop

if __name__ == '__main__':
    HBNBCommand().cmdloop()
