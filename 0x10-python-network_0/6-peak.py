#!/usr/bin/python3
"""Find the peak in a given list"""


def find_peak(list_of_integers):
    """Find peak"""
    max_num = list_of_integers[0]
    for i in range(1, len(list_of_integers)):
        if list_of_integers[i] > max_num:
            max_num = list_of_integers[i]
    return (max_num)
