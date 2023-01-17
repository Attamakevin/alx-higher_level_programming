#!/usr/bin/python3

"""this module represents the “base” of all other 
classes in this projet
"""


class Base:
    """This class will be the “base” of all other classes in this project"""

    __nb_objects = 0
    """initializing the base"""

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
