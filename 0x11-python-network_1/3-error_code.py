#!/usr/bin/python3
"""Module to send and handles Error using urllib"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read()
            content = res.decode('utf8')
            print(content)
    except urllib.error.URLError as e:
        print("Error code:", e.code)
