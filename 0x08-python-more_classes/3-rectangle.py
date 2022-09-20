#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("heigh must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []

        for i in range(self.__height):
            for j in range(self.__width):
                rect.append("#")
            rect.append("\n")
        return ("".join(rect))
