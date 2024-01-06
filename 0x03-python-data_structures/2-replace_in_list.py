#!/usr/bin/python3
def replace_in_list(my_list, index, element):
    if index < 0 or index >= len(my_list):
        return my_list
    my_list[index]=element
    return my_list
