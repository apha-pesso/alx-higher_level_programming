#!/usr/bin/python3
"""Square Class"""


class Square():
    """Square class"""
    def __init__(self, size=0):
        """Initialize size"""
        self.__size = size

    @property
    def size(self):
        """Retrieves size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the value for size"""
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute and return area"""
        return (self.__size ** 2)
