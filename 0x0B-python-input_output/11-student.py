#!/usr/bin/python3
"""Class that defines student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize the object
        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns json repr of the object"""
        if not attrs:
            return (self.__dict__)

        new = {}
        for att in attrs:
            if att in self.__dict__:
                new[att] = self.__dict__[att]
        return new

    def reload_from_json(self, json):
        """Replace all attributes of student instamce"""
        for key, value in json.items():
            setattr(self, key, value)
