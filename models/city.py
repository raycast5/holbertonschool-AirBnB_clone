#!/usr/bin/python3
""""Module containing a class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A new class called City

    Attributes:
    state_id: (str): empty string - it will be the State.id
    name: (str): empty string

    """

    state_id = ""
    name = ""
