#!/usr/bin/python3
"""Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Displays Rectangle in shapes"""
        for i in range(self.y):
            print()
        for i in range(self.__height):
            for _ in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            if i != self.height:
                print()

    def __str__(self):
        """Prints preset formated display"""
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Assigns variable using *args"""
        if args:
            if len(args) == 1:
                self.id = args[0]

            elif len(args) == 2:
                self.id = args[0]
                self.__width = args[1]

            elif len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]

            elif len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]

            else:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v

                elif k == "width":
                    self.__width = v

                elif k == "height":
                    self.__height = v

                elif k == "x":
                    self.__x = v

                else:
                    self.__y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
