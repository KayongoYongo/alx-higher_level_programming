#!/usr/bin/python3

"""defines a base class"""
import json


class Base:
    """defined a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        my_dict = list_objs.to_dictionary()
        my_json_string = to_json_string([my_dict])

        with open(self.__class__.__name__ as f:
