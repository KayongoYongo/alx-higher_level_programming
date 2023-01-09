#!/usr/bin/python3
"""subclass checker"""


def inherits_from(obj, a_class):
    """returns subclass yes"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
