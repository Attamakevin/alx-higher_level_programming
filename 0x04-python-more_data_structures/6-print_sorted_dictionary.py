#!/usr/bin/python3
# a function that prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    dic_sort = (a_dictionary.keys())
    sorted (dic_sort)
    for i in dic_sort:
        print("{}: {}". format(i, a_dictionary.get(i)))
