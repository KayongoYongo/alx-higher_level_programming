#!/usr/bin/python3
for i in range(0, 99):
    if i % 10 < i / 10:
        continue
    if i == 89:
        print("{:d}".format(i))
    else:
        print("{:02d}".format(i), end=", ")
