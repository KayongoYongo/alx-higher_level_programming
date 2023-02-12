#!/usr/bin/python3
"""We need this module to convert a python object into json representation"""
import json


def to_json_string(my_obj):
    """json.dumps() is used to convert a python object into a JSON string
    json.dump() is used to write to a json file
    """
    return (json.dumps(my_obj))

