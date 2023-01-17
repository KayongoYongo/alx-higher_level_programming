#!/usr/bin/python3

"""rectangle class inheriting from base"""
from models.base import Base


class Rectangle(Base):
    """defined rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes of an instance of the class"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):

        """Returns width"""
        return self.__width

    @width.setter
    def width(self, width):

        """setter for width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):

        """Returns area height"""
        return self.__height

    @height.setter
    def height(self, height):

        """setter for height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise valueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):

        """Returns x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):

        """Returns y"""
        return self.__y

    @y.setter
    def y(self, y):

        """setter for y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):

        """returns the rectangle area"""
        return self.__height * self.__width

    def display(self):
        """a function to display the rectangle"""

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """returns a string representation of the object"""

        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """updates the object with different values"""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a ductionary representation of the object"""
        return {"x": self.x, "y": self.y,
                "id": self.id, "height": self.height, "width": self.width}
