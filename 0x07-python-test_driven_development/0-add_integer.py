#!/usr/bin/python3
"""Add function"""


def add_integer(a, b):
    """returns the sum of a and b
    a and b must be either integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
