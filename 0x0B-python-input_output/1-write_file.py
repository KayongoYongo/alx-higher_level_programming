#!/usr/bin/python3
"""returns number of lines"""


def write_file(filename="", text=""):
    """number of lines"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return (f.write(text))
