#!/usr/bin/python3


"""an empty class Square that defines a square"""


class Square:

    """an empty class"""
    def __init__(self, size=0):

        """initilization of new square.
        Args:
        size (int): the size of the new square"""
        self.size = size

    @property
    def size(self):
        """get/set the current size of a square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """defining area of square"""

        return (self.__size**2)
