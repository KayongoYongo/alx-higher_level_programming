#!/usr/bin/python3

def append_write(filename="", text=""):

    with open(filename, 'a+', encoding='utf-8') as f:
        """With a+, if the file does not exist in the directory,
        The file will be created automatically
        """
        return (f.write(text))
