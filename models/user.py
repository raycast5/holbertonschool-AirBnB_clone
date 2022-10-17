#!/usr/bin/python3
""""Module containing a class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A new class called User

    Attributes:
    email (str): User's email
    password (str): User's password
    first_name (str): User's first name
    last_name (str): User's last name

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
