#!/usr/bin/python3
"""Define a square from REctangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class from rectangle"""
    def __init__(self, size):
        """Initialize the square
        Args:
            size- size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """print string format"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
    # def area(self):
    #     """Returns area of the square"""
    #     return (self.__size ** 2)
