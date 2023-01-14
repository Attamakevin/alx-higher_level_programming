#!/usr/bin/python3


"""a module that append a string to a text file
   (UTF8) and returns the number of characters written
"""


def append_write(filename="", text=""):
    """writes a string to a textfile and return no of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        num_of_char_appended = f.write(text)
    return(num_of_char_appended)
