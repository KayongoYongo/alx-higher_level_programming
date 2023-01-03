#!/usr/bin/python3
""" Creating a class called Rectangle"""


class Rectangle:
    """Make rectangle object"""

    def __init__(self, width=0, height=0):
        """Make a new rectangle object"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """gets width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return areas of a rectangle."""
        return(self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        return((self.__width + self.__height) * 2)	
