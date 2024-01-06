#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list):
        return None
    max_value = my_list[0]
    for i in range(len(my_list)):
        if my_list >= max_value:
            max_value = my_list
    return max_value
