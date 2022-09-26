#!/usr/bin/python3
"""Special int class"""


class MyInt(int):
    """My integer claass"""
    def __eq__(self, value):
        """change the operation"""
        return self.real != value

    def __ne__(self, value):
        """change the operation"""
        return self.real == value
