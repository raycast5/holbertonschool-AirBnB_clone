#!/usr/bin/python3
""""Module containing a class"""
import json
from datetime import datetime

from models.base_model import BaseModel


class FileStorage:
    """
    A new class called FileStorage
    that saves files
    """

    def __init__(self):
        """Initializes function"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        new_dict = {}
        with open(self.__file_path, "w+", encoding="utf-8") as f:
            for k, v in self.__objects.items():
                new_dict[k] = v.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                o_dict = json.loads(f.read())
                for k, v in o_dict.items():
                    inst = eval(v["__class__"])(**v)
                    self.__objects[k] = inst
        except Exception:
            pass
