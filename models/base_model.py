#!/usr/bin/python3
""""Module containing a class"""

from datetime import datetime
import json
from uuid import uuid4

class BaseModel:
    """A new class called Base"""

    def __init__(self):
        """Initialization method"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of base"""

        return (f"[BaseModel] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the update time"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict of the instance"""

        inst_dict = self.__dict__
        inst_dict.update({"__class__": "BaseModel"})
        inst_dict["created_at"] = (self.created_at.isoformat())
        inst_dict["updated_at"] = (self.updated_at.isoformat())
        return inst_dict
