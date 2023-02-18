#!/usr/bin/python3

import sys
count = len(sys.argv) - 1
total = 0

for i in range(count):
    total += int(sys.argv[i + 1])
    """I have to do sys.argv[i].
    This is because the arguments are stored in a list.
    ---Moreover, I have to type cast it into int.
    This is because the list of arguments are stored as strings by defult.
    ---Additionally, I have to set the element as [i + 1].
    The first element of the list is the name of the program.
    Trying to use it in addition will result to an error.
    This is because it does not have the same type as the other integers"""

print("{}".format(total))
