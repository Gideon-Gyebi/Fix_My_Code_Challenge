#!/usr/bin/python3
"""This is the quare module."""


class square():
    """The square class."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Init sequence."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """ The area of the square """
        return self.width * self.height

    def perimeter(self):
        """ The perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """The string representation."""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter())
