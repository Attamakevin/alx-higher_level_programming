#!/usr/bin/python3


"""an empty class Square that defines a square"""


class Square:

    """an empty class"""
    def __init__(self, size=0):

        """initilization of new square.
        Args:
        size (int): the size of the new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
