#!/usr/bin/python3
"""Mylist class inherited from List"""


class MyList(list):
    """Mylist class"""
    
    def print_sorted(self):
        """This will return a sorted list in ascending order"""
        print (sorted(self))
