#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Base class for the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Object Initialization"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json representation of the list_dictionaries"""
        if (list_dictionaries is None or list_dictionaries == []):
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json string to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as new_file:
            if list_obj is None:
                new_file.write("[]")
            else:
                list_dicts = [item.to_dictionary() for item in list_objs]
                new_file.write(Base.to_json_string(list_dicts))
