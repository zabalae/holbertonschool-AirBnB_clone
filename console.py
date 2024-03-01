#!/usr/bin/python3
'''Contains the entry point of the command interpreter'''


import cmd
import json
#import os
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file_path = 'file.json'
    classes = {'BaseModel': BaseModel, 'User': User,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Place': Place, 'Review': Review}

    def do_quit(self, arg):
        '''Will exit the program'''
        return True

    def do_EOF(self, arg):
        '''Will exit the program'''
        print()
        return True

    def do_help(self, arg):
        '''Will show help'''
        super().do_help(arg)

    def emptyline(self):
        '''Do nothing when input is empty line'''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it
            (to the JSON file), and prints the id
        '''
        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[arg]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def do_show(self, arg):
        '''Prints the string representation of an instance based on
            the class name and id
        '''
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif '{}.{}'.format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            key = '{}.{}'.format(args[0], args[1])
            content = storage.all()[key]
            print(content)

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id (save the
            change into the JSON file)
        '''
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif '{}.{}'.format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            key = '{}.{}'.format(args[0], args[1])
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        '''Prints all str representation of all instances based or not
            on the class name
        '''
        args = shlex.split(arg)
        dict_t = storage.all()

        if not args:
            print([str(value) for value in dict_t.values()])
            return
        if args[0] in self.classes:
            print([str(value) for key, value in dict_t.items()
                   if key.split(".")[0] == args[0]])
            return
        print("** class doesn't exist **")

    def do_update(self, arg):
        '''Updates an instance based on the class name and id by adding
            or updating attribute
        '''
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        storage.reload()
        dict_objs = storage.all()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            key = args[0] + "." + args[1]
            dict_objs[key]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = dict_objs[key]
        if hasattr(obj, args[2]):
            data_type = type(getattr(obj, args[2]))
            setattr(obj, args[2], data_type(args[3]))
        else:
            setattr(obj, args[2], args[3])
        storage.save()

    def precmd(self, line):
        '''Will execute before each command'''
        if '.' not in line:
            return line
        cmd, arg = line.split('.', 1)
        arg = arg.replace('(', ' ')
        arg = arg.replace(')', ' ')
        line = cmd + ' ' + arg
        return line

    # def postcmd(self, stop, line):
    #     '''Will execute after each command'''
    #     BaseModel.save_to_file()
    #     return stop


if __name__ == '__main__':
    HBNBCommand().cmdloop()
