#!/usr/bin/python3
for char in range(26):
    if char >= 97 and char < 123:
        print("{:s}".format(chr(char + ord("a"))), end="")
