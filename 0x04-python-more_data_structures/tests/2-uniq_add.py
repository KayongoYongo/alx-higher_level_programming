#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    total = 0
    for i in new_list:
        total += i
    return total
