#!/usr/bin/python3

"""Prints a list from a class"""


class MyList(list):
    """defined a class inheriting from list"""
    def print_sorted(self):
        print(sorted(self))
