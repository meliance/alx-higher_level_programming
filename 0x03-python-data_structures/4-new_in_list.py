#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 and idx >= len(my_list):
        new_list = my_list.copy()
        return new_list
    new_list[idx] = element
    return new_list