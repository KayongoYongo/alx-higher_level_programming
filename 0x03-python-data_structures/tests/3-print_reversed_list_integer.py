#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list[::-1]
    [print("{:d}".format(i)) for i in reversed_list]
