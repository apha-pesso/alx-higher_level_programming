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

    def to_json(self):
        """Returns json repr of the object"""
        return (self.__dict__)
