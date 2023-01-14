#!/usr/bin/python3
"""a module that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file"""
    with open(filename, mode = 'r', encoding = "utf-8") as f:
        for line in f:
            print(line)
