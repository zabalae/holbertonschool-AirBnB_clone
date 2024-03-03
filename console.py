#!/usr/bin/python3
'''Contains the entry point of the command interpreter'''


import cmd
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
    classes = {'BaseModel': BaseModel, 'User': User,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Place': Place, 'Review': Review}

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''Will exit the program using Ctrl-D'''
        print()
        return True

    # def do_help(self, arg):
    #     '''Will show help'''
    #     super().do_help(arg)

    def emptyline(self):
        '''Do nothing when input is empty line'''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it
            (to the JSON file), and prints the id
        '''
        if not arg:
            print("** class name missing **")
        elif arg in HBNBCommand.classes:
            new_instance = HBNBCommand.classes.get(arg)()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        '''Prints the string representation of an instance based on
            the class name and id
        '''
        args = arg.split(" ")
        if not args:
           print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
           print("** class doesn't exist **")
        elif len(args) == 1:
           print("** instance id missing **")
        else:
            content = storage.all()
            key = '{}.{}'.format(args[0], args[1])
            if key in content.keys():
                print(content[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id (save the
            change into the JSON file)
        '''
        args = arg.split(" ")
        if args[0] == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            content = storage.all()
            key = '{}.{}'.format(args[0], args[1])
            if key in content.keys():
                del content[key]
            else:
                print("** no instance found **")

    def do_all(self, arg):
        '''Prints all str representation of all instances based or not
            on the class name
        '''
        if (arg == ""):
            args = list(storage.all().values())
            print(list(map(lambda x: str(x), args)))
        elif arg in HBNBCommand.classes:
            args = list(storage.all().values())
            args = filter(lambda x: type(x) is
                              HBNBCommand.classes.get(arg), args)
            print(list(map(lambda x: str(x), args)))
        else:
            print("** class doesn't exist **")
        
    def do_update(self, arg):
        '''Updates an instance based on the class name and id by adding
            or updating attribute
        '''
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif not args[0] in HBNBCommand.name_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])
              not in storage.all().keys()):
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            content = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in content.keys():
                attr = getattr(content[key], args[2], "")
                setattr(content[key], args[2], type(attr)(args[3]))
                content[key].save()

    @staticmethod
    def all_class(*args):
        '''call all instaces of obj'''
        tmp = HBNBCommand()
        tmp.do_all(args[0])

    funcs = {".all()": "HBNBCommand.all_class",
             ".count()": "HBNBCommand.count_class",
             ".show()": "HBNBCommand.show_class",
             ".destroy()": "HBNBCommand.destroy_class",
             ".update()": "HBNBCommand.update_class"}

    def do_User(self, arg):
        '''functions for User:'''
        cmd_args = arg[arg.find("(") + 1:arg.find(")")]
        cmd_line = arg.replace(cmd_args, "")
        if cmd_line in HBNBCommand.funcs:
            eval(HBNBCommand.funcs[cmd_line] + "({})"
                 .format("'User', " + cmd_args))
            
    def do_BaseModel(self, arg):
        '''functions for BaseModel:'''
        cmd_args = arg[arg.find("(") + 1:arg.find(")")]
        cmd_line = arg.replace(cmd_args, "")
        if cmd_line in HBNBCommand.funcs:
            eval(HBNBCommand.funcs[cmd_line] + "({})"
                 .format("'BaseModel', " + cmd_args))
            
    def do_State(self, arg):
        '''functions for State:'''
        cmd_args = arg[arg.find("(") + 1:arg.find(")")]
        cmd_line = arg.replace(cmd_args, "")
        if cmd_line in HBNBCommand.funcs:
            eval(HBNBCommand.funcs[cmd_line] + "({})"
                 .format("'State', " + cmd_args))

    def do_City(self, arg):
        '''functions for City:'''
        cmd_args = arg[arg.find("(") + 1:arg.find(")")]
        cmd_line = arg.replace(cmd_args, "")
        if cmd_line in HBNBCommand.funcs:
            eval(HBNBCommand.funcs[cmd_line] + "({})"
                 .format("'City', " + cmd_args))
            
    def do_Place(self, arg):
        '''functions for Place:'''
        cmd_args = arg[arg.find("(") + 1:arg.find(")")]
        cmd_line = arg.replace(cmd_args, "")
        if cmd_line in HBNBCommand.funcs:
            eval(HBNBCommand.funcs[cmd_line] + "({})"
                 .format("'Place', " + cmd_args))
            
    def do_Amenity(self, arg):
        '''functions for Amenity:'''
        cmd_args = arg[arg.find("(") + 1:arg.find(")")]
        cmd_line = arg.replace(cmd_args, "")
        if cmd_line in HBNBCommand.funcs:
            eval(HBNBCommand.funcs[cmd_line] + "({})"
                 .format("'Amenity', " + cmd_args))
            
    def do_Review(self, arg):
        '''functions for Review:'''
        cmd_args = arg[arg.find("(") + 1:arg.find(")")]
        cmd_line = arg.replace(cmd_args, "")
        if cmd_line in HBNBCommand.funcs:
            eval(HBNBCommand.funcs[cmd_line] + "({})"
                 .format("'Review', " + cmd_args))
            
    @staticmethod
    def count_class(*args):
        '''count all instaces'''
        list_obj = list(storage.all().values())
        list_obj = filter(lambda x: type(x) is
                          HBNBCommand.classes.get(args[0]), list_obj)
        print(len(list(list_obj)))

    @staticmethod
    def show_class(*args):
        ''' show an intances '''
        tmp = HBNBCommand()
        tmp.do_show(" ".join(args))

    @staticmethod
    def destroy_class(*args):
        ''' destroy an intance '''
        tmp = HBNBCommand()
        tmp.do_destroy(" ".join(args))

    @staticmethod
    def update_class(*args):
        ''' update an intance '''
        tmp = HBNBCommand()
        if len(args) == 3 and type(args[2]) is dict:
            for attr, val in args[2].items():
                temp = list(args[0:2]) + [attr, str(val)]
                tmp.do_update(" ".join(temp))
        else:
            tmp.do_update(" ".join(args))


    # def do_count(self, arg):
    #    '''Retrieves the number of instances of a class'''
    #    args = shlex.split(arg)
    #    if not args:
    #        print("** class name missing **")
    #    elif args[0] not in self.classes:
    #        print("** class doesn't exist **")
    #    else:
    #        class_name = args[0]
    #        instances = storage.get_all(self.classes[class_name])
    #        count = len(instances)
    #        print(count)

    # def precmd(self, line):
    #     '''Will execute before each command'''
    #     if '.' not in line:
    #         return line
    #     cmd, arg = line.split('.', 1)
    #     arg = arg.replace('(', ' ')
    #     arg = arg.replace(')', ' ')
    #     line = cmd + ' ' + arg
    #     return line

    # def postcmd(self, stop, line):
    #    '''Will execute after each command'''
    #    BaseModel.save_to_file()
    #    return stop


if __name__ == '__main__':
    HBNBCommand().cmdloop()