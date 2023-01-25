#!/usr/bin/python3

old_list = [1, 2, 3, 4, 5]
new_list = old_list[:]
new_list[0] = 6
print(old_list) # [1, 2, 3, 4, 5]
print(new_list) # [6, 2, 3, 4, 5]

