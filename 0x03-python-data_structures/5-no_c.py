#!/usr/bin/python3
def def no_c(my_string):
    without_c = []
    for char in my_string:
        if char != 'c' and char != 'C':
            without_c.append(char)
    return ' '.join(without_c)
