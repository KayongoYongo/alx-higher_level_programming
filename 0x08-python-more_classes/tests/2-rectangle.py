#!/usr/bin/python3
"""Create an empty rectangle class"""


class Rectangle:
    """Create Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize attributes of rectangle.
            Args:
            width (int): The width of a rectangle.
            height (int): The height of a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retreives the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retreives the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self): 
        """Returns the area of a rectangle"""
        return (self.__width * self.height)

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return ((self.__width + self.__height) * 2)
