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

    @property
    def size(self):
        """Get the size for the squar"""
        return (self.width)

    @size.setter
    def size(self, value):
        """if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__size = value
            """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square attributes with the arguments"""
        if args:
            for arg in args:
                n = 0
                if n == 0:
                    self.id = arg

                elif n == 1:
                    self.arg

                elif n == 2:
                    self.x = arg

                elif a == 3:
                    self.y = arg

                n += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v

                elif k == "size":
                    self.size = v

                elif k == "x":
                    self.x = v

                elif k == "y":
                    self.y = v

    def __str__(self):
        """Prints preset formated display"""
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.size))
