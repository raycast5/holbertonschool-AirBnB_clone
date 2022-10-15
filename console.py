#!/usr/bin/python3
""""Module containing a class"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quits program"""
        quit()

    def do_EOF(self, args):
        """Quits program"""
        quit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
