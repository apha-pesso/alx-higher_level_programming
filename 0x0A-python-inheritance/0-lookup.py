#!/usr/bin/python3
"""Function to return list of attributes and methods"""


def lookup(obj):
    """This function will return the
    available attributes and methods
    Args: obj- the object to check
    Return: List of attributes"""

    return dir(obj)
