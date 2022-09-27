#!/usr/bin/python3
"""Function that read and prints to stdout"""


def read_file(filename=""):
    """Reads the content of the file
    and prints to stdout
    """
    with open("filename", encoding="utf-8") as w:
        a = w.read()
    print(a, end="")
