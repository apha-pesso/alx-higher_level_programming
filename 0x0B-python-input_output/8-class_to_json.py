#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """The function will return a dictionary description
    of an object
    Args:
        obj- object to return
    Return:
        Return json
    """
    return (obj.__dict__)
