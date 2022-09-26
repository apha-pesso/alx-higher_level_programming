#!/usr/bin/python3
"""Only subclass"""


def inherits_from(obj, a_class):
    """Only subclass of the class
    Args:
        obj- Object to test
        a_class- class to check
    Return:
        returns True if it is subclass
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
