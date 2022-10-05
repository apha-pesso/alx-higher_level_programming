#!/usr/bin/python3
"""Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square object"""
        super().__init__(size, size, x, y, id)
        self.size = size
        # self.size = height

    def __str__(self):
        """Prints preset formated display"""
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.size))
