#!/usr/bin/python3
"""Module to send a POST request using usrllib"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    url = argv[1]
    value = {}
    value['email'] = argv[2]
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        res = response.read()
        content = res.decode('utf8')
    print(content)
