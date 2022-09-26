#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        """Area method that raises error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
