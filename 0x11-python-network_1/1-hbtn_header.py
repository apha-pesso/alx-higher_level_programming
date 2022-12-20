#!/usr/bin/python3
"""Moule to fetch status"""
# Python script that fetches https://alx-intranet.hbtn.io/status


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        head = req.headers
    dict(head)
    print(head['X-Request-Id'])
