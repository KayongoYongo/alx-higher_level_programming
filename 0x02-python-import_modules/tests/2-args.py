#!/usr/bin/python3

import sys

if __name__ == "__main__":
    count  = len(sys.argv) - 1
    """The -1 is there to skip the name of the function"""
    
    if count == 1:
        print("{} argument".format(count))
    else:
        print("{} arguments".format(count))
        for i in range(count):
            print("{} : {} ".format(i + 1, sys.argv[i + 1]))

