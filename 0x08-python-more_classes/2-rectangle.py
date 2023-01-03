#!/usr/bin/python3


"""a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:

    """rectangle class"""
    def __init__(self, width=0, height=0):

        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def height(self):

        """get the current height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):

        """set current height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """get the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set curent width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """return area of rectangle"""

        return self.__width * self.__height
    def perimeter(self):
        """return perimeter of rectangle"""

        if self.__height != 0 or self.__width != 0:
            return (self.height + self.width) * 2
        return 0
