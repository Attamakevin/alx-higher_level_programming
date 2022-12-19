#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        ret = 0
        for i in range(x):
            print("{}".format(my_list[i]),end=" ")
            ret += 1
        except IdexError:
            break
    return(ret)
