#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """initialize the height and width"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set value for the width"""
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set value for height"""
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
