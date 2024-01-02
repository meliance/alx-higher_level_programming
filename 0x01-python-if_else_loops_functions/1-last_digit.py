#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
my_num = str(number)[-1]  # Convert to string and get the last character

if int(my_num) > 5:
    print(f'Last digit of {number} is {my_num} and is greater than 5')
elif int(my_num) == 0:
    print(f'Last digit of {number} is {my_num} and is 0')
else:
    print(f'Last digit of {number} is {my_num} and is less than 6 and not 0')
