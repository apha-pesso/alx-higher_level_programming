#!/usr/bin/python3
"""Function to add attricbute"""


def add_attribute(obj, att, value):
    """Adds new attribute if possible
    Raise:
        TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
