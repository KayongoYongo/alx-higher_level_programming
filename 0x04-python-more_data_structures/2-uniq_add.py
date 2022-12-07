#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    add = 0
    for i in a:
        add += i
    return add
