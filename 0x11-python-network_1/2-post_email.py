#!/usr/bin/python3
"""Post email"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')

    print(body)
