#!/usr/bin/python3
"""Look up the list of attributes and objects"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
