#!/usr/bin/python3
def no_c(my_string):
    without_c_string = []
    for char in my_string:
        if char != 'c' and char != 'C':
            without_c_string.append(char)
    return ''.join(without_c_string)
