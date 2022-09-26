#!/usr/bin/python3
"""Function to check instance"""


def is_same_class(obj, a_class):
    """Checks if and object is an instance of the class
    Args:
        obj- object to be tested
        a_class- class to check against
    Return: Returns True is isinstance
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
