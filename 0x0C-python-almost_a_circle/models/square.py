#!/usr/bin/python3

"""square class inherting from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defined a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return("[Square] ({}) {}/{} - {}\
                ".format(self.id, self.x, self.y, self.__size))

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.width = value
        self.heigh = value
        self.__size = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {"id": self.id, "x": self.x,
                "size": self.size, "y": self.y}
