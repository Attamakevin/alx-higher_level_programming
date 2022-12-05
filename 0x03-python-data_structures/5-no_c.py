#!/usr/bin/python3
def no_c(my_string):
    for i in len(my_string):
        new_string = my_string.remove('cC')
        return new_string
