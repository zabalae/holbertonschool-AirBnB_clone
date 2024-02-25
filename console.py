#!/usr/bin/python3
'''Contains the entry point of the command interpreter'''

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
