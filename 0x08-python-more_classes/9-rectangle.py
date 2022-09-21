#!/usr/bin/python3
"""reactangle class"""


class Rectangle:
    """Reactangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize ractangle
        args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Return printable representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append(str(self.print_symbol))
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return a string representation of the rectangle"""
        r = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return r

    def __del__(self):
        """print message after deleting rectangle instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area
        Args:
            rect_1: rectangle 1
            rect_2: rectangle 2
        if rect_1 is not instance of Rectangle
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_2 is not instance of Rectangle
            raise TypeError("rect_2 must be an instance of Rectangle")
        Return rect1 if both have the same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        width = size
        height = size
        return cls(width, height)
