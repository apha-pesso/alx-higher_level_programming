#!/usr/bin/python3
"""Create square class with Area"""


class Square():
    """Square class"""
    def __init__(self, size=0):
        """Initialize size"""
        self.__size = size
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """Return square of value size"""
        return (self.__size ** 2)
