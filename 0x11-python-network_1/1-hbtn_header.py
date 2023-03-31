#!/usr/bin/python3
"""Display the value of an x-request ID"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')

    print(x_request_id)
