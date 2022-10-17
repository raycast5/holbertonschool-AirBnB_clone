#!/usr/bin/python3
""""Module containing a class"""
import copy
import json
from datetime import datetime
from uuid import uuid4

import models


class BaseModel:

    """A new class called Base"""

    def __init__(self, *args, **kwargs):
        """Initialization method"""
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ('created_at', 'updated_at'):
                        setattr(self, k, datetime.strptime(
                            v, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of base"""

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the update time"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dict of the instance"""

        inst_dict = copy.deepcopy(self.__dict__)
        inst_dict.update({"__class__": f"{self.__class__.__name__}"})
        inst_dict["created_at"] = (self.created_at.isoformat())
        inst_dict["updated_at"] = (self.updated_at.isoformat())
        return inst_dict
