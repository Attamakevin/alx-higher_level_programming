#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """a function that replaces an element of a list at a specific position"""
   for idx in my_list:
	if idx < 0 or idx > len(my_list):
	    return my_list
        else:
	    element = my_list[idx]
	    return my_list
