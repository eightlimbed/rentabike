#!/usr/bin/python3
'''
This file contains the code for the rentabike console. The console is an
administrative command-line tool for managing objects that interprets the
following commands:

'''
import cmd
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.bike import Bike
from models.state import State
from models.city import City
from models.category import Category
from models.review import Review
import shlex


class Console(cmd.Cmd):
    '''
    Contains all methods (commands) for the rentabike admin console.
    '''
    prompt = ('(rentabike) ')

    def do_quit(self, args):
        '''
        Quit command to exit the program.
        '''
        return True

    def do_EOF(self, args):
        '''
        Exits after receiving the EOF signal.
        '''
        return True

    def do_create(self, args):
        '''
        Creates a new instance of class BaseModel and saves it to storage.
        '''
        if len(args) == 0:
            print('** class name missing **')
            return
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except:
            print('** class doesn\'t exist **')

    def do_show(self, args):
        '''
        Prints the string representation of an instance based on the class name
        and id given as args.
        '''
        args = shlex.split(args)
        if len(args) == 0:
            print('** class name missing **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print('** class doesn\'t exist **')
            return
        key = args[0] + '.' + args[1]
        key = args[0] + '.' + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print('** no instance found **')

    def do_destroy(self, args):
        '''
        Deletes an instance based on the class name and id.
        '''
        args = shlex.split(args)
        if len(args) == 0:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        class_name = args[0]
        class_id = args[1]
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(class_name)
        except NameError:
            print('** class doesn\'t exist **')
            return
        key = class_name + '.' + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print('** no instance found **')
        storage.save()

    def do_all(self, args):
        '''
        Prints all instances to stdout based on the class name.
        '''
        obj_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print('** class doesn\'t exist **')
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(obj_list)

    def do_update(self, args):
        '''
        Updates an instance based on the class name and id passed as args.
        '''
        storage = FileStorage()
        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        elif len(args) == 2:
            print('** attribute name missing **')
            return
        elif len(args) == 3:
            print('** value missing **')
            return
        try:
            eval(args[0])
        except NameError:
            print('** class doesn\'t exist **')
            return
        key = args[0] + '.' + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print('** no instance found **')
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()

    def emptyline(self):
        '''
        Prevents printing anything when an empty line is passed.
        '''
        pass

    def do_count(self, args):
        '''
        Prints the number of instances in storage.
        '''
        obj_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print('** class doesn\'t exist **')
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(len(obj_list))

    def default(self, args):
        '''
        Catches all the function names that are not expicitly defined.
        '''
        functions = {'all': self.do_all, 'update': self.do_update,
                     'show': self.do_show, 'count': self.do_count,
                     'destroy': self.do_destroy, 'update': self.do_update}
        args = (args.replace('(', '.').replace(')', '.')
                .replace('\'', '').replace(',', '').split('.'))
        try:
            cmd_arg = args[0] + ' ' + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except:
            print('*** Unknown syntax:', args[0])


if __name__ == '__main__':
    '''
    Entry point for the console.
    '''
    Console().cmdloop()
