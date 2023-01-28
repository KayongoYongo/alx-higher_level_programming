#!/usr/bin/python3
"""Create a new class called square"""


class Square:
    """Initialize a new square with size"""

    def __init__(self, size=0):
        """Initialize a square.
        Args:
            size (int): The size of a new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrives the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """"Sets the value of the size to value.
        Args:
            value (int): The set value of the size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Finds the area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a square"""
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
