#!/usr/bin/python3

"""Print the alphabet in lowercase, not followed by a new line."""

for i in range(97, 123):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    print("{}".format(chr(i)), end="")
