#!/usr/bin/python3
'''
    console module
'''
import cmd


class HBNBCommand(cmd.Cmd):
    ''' The console class '''
    prompt = "(hbnb)"

    def do_quit(self, line):
        ''' quit command to exit the program'''
        return True

    def emptyline(self):
        return None

    def do_create(self, class_name):
        ''' Creates a new instance of BaseModel '''
        the_model = class_name()
        the_model.save()
        print(the_model.id)

    def do_EOF(self, line):
        ''' exits the program '''
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
