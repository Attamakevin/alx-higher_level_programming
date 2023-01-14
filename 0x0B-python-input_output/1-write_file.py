#!/usr/bin/python3


"""a module that writes a string to a text file
   (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a string to a textfile and return no of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        num_of_char_written = f.write(text)
    return(num_of_char_written)
