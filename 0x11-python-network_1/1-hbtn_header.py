#!/usr/bin/python3
"""Moule to fetch response header using usrllib"""
# Python script that fetches https://alx-intranet.hbtn.io/status


if __name__ == "__main__":
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as req:
        head = req.headers
    dict(head)
    print(head['X-Request-Id'])
