#!/usr/bin/python3
"""making an http post request"""

import requests
from sys import argv

if __name__ == "__main__":
    data = {'email': argv[2]}
    response = requests.post(argv[1], data)
    print(response.text)
