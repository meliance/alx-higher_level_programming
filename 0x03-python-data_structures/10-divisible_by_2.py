#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mult_2.append(True)
        else:
            mult_2.append(False)
    return mult_2
