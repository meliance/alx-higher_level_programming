#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        new_list = []
        for i in range(len(my_list)):
            if my_list[i] != idx:
                new_list.append(i)
        return new_list
