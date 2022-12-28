#!/usr/bin/python3
"""Print all possible different combinations of two digits in ascending order.
    The two digits must be different - 01 and 10 are considered identical.
    """
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
