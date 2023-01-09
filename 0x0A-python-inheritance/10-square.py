#!/usr/bin/python3

"""inherits from Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defined a square"""

    def __init__(self, size):
        """initialize a new rectangle"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] " + str(self.__size) + "/" + str(self.__size)
