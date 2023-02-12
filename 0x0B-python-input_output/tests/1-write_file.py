#!/usr/bin/python3

def write_file(filename="", text=""):
    """The function takes in two parameters"""
    with open(filename, 'w+', encoding='utf-8') as f:
        """Note: r+ and w+ do the same thing. 
        They open the file for reading and writing puposes.
        Howerver, r+ only works when te file exists.
        If the file doesn't exist, we use w+.
        w+ creates that file even if its not available in the environment
        """
        return (f.write(text))
