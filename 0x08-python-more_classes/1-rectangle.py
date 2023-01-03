#!/usr/bin/python3
""" Creating a class claaed Rectangle"""


class Rectangle:
    """Instatiation of the class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Using Property to get the value of width"""

    @property
    def width(self):
        return (self.__width)

    """Using .setter to mutate the value of width"""

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Using property to get the value of height"""
    @property
    def height(self):
        return (self.__height)

    """Using seter to mutate the value of height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an iteger")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
