#!/usr/bin/python3
""""Module containing a class"""

import cmd

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_names = ["BaseModel"]

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Quits program"""
        quit()

    def do_EOF(self, args):
        """Quits program"""
        quit()

    def do_create(self, args):
        """Creates new instance"""
        args= args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        else:
            new_class = eval(args[0])()
            new_class.save()
            print(f"{new_class.id}")

    def do_show(self, args):
        """Shows string representation of instance"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            fullname = args[0] + "." + args[1]
            inst_list = storage.all()
            if fullname not in inst_list.keys():
                print("** no instance found **")
            else:
                print(inst_list[fullname])

    def do_destroy(self, args):
        """Destroys an instance"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            fullname = args[0] + "." + args[1]
            inst_list = storage.all()
            if fullname not in inst_list.keys():
                print("** no instance found **")
            else:
                del inst_list[fullname]
                storage.save()
    
    def do_update(self, args):
        """Updates an instance with specified parameters"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            fullname = args[0] + "." + args[1]
            inst_list = storage.all()
            if fullname not in inst_list.keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                setattr(inst_list[fullname], args[2], args[3])
                storage.save()


    def do_all(self, args):
        args = args.split()
        inst_dic = storage.all()
        class_list = []
        if len(args) == 0:
            for v in inst_dic.values():
                class_list.append(str(v))
        else:
            if args[0] not in HBNBCommand.class_names:
                print("** class doesn't exist **")
                return
            else:
                for v in inst_dic.values():
                    if v.__class__.__name__ == args[0]:
                        class_list.append(str(v))
        print(class_list)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
