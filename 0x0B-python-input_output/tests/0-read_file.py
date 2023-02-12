#!/usr/bin/python3
"""this is the read file function"""


def read_file(filename=""):
    """The with keyword is very crucial.
    The file closes properly eve after an exception is raised.
    r - shows that the file is only open for reading.
    utf-8 is the default encoder.
    f is the final file object
    """
    with open('my_file_0.txt', 'r', encoding='utf-8') as f:
        """To read the contents line by line, I use the for loop.
        This is fast and memory efficient and leads to simple code.
        """
        for line in f:
            print(line, end='')
