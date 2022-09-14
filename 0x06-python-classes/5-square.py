#!/usr/bin/python3
"""Square Class"""


class Square():
    """Square class"""

    def __init__(self, size=0):
        """Initialize size"""
        self.__size = size

    def area(self):
        """Returns Area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Retireve the size value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set value for size"""
        if (type(value) != int):
            raise TypeError("size must be an integer")

        elif (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Prints to stdout"""
        a = self.__size
        if a == 0:
            print()
        for i in range(a):
            for j in range(a):
                print("#", end="")
            print()
