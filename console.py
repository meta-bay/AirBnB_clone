#!/usr/bin/python3
'''
    console module
'''
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    ''' The console class '''
    prompt = "(hbnb) "

    def do_quit(self, line):
        ''' quit command to exit the program'''
        return True

    def emptyline(self):
        return None

    def do_create(self, class_name):
        ''' Creates a new instance of BaseModel '''
        if not class_name:
            print("** class name missing **")
            return

        try:
            my_object = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        new_instance = my_object()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        ''' Prints the string representation of an instance '''
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()

        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = None

        if len(args) > 1:
            instance_id = args[1]

        try:
            my_object = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        storage.reload()
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        ''' Deletes an instance '''
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()

        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = None

        if len(args) > 1:
            instance_id = args[1]

        try:
            my_object = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        storage.reload()
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        ''' Prints all string representation of all instances '''
        storage.reload()
        obj_list = []

        if not arg:
            for key, value in storage.all().items():
                obj_list.append(str(value))
            if obj_list:
                print(obj_list)
            return
        class_name = arg
        try:
            my_object = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if value.__class__ == my_object:
                obj_list.append(str(value))
                print(obj_list)

    def do_update(self, arg):
        ''' Updates an instance by adding
            or updating attribute
        '''
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()

        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = None
        attr = None
        attr_val = None

        if len(args) >= 4:
            class_name = args[0]
            instance_id = args[1]
            attr = args[2]
            attr_val = args[3]

        try:
            my_object = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        storage.reload()
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            obj = storage.all()[key]
            if hasattr(obj, attr):
                setattr(obj, attr, type(getattr(obj, attr))(attr_val))
            else:
                setattr(obj, attr, attr_val)
            obj.save()
        else:
            print("** no instance found **")

    def do_EOF(self, line):
        ''' exits the program '''
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
