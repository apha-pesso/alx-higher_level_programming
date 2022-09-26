#!/usr/bin/python3
"""Check if object is an instance"""


def is_kind_of_class(obj, a_class):
    """Check if an object is from a class"""
    if isinstance(obj, a_class):
        return True
    else: return False
