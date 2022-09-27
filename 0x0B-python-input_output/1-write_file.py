#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """Write to a file
    overwrite the file if it exists"""
    with open("filename", "w", encoding="utf-8") as w:
        a = w.write(text)
    return a
