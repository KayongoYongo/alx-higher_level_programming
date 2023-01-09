#!/usr/bin/python3
"""checks for type of class against object"""


def is_same_class(obj, a_class):
    """Returns:
    If obj is exactly an instance of a_class - True.
    Otherwise - False."""
    if type(obj) == a_class:
        return True
    return False
