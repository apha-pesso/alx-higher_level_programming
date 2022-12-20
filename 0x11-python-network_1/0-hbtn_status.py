#!/usr/bin/python3
"""Moule to fetch status"""
# Python script that fetches https://alx-intranet.hbtn.io/status

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        content = req.read()
        utf_content = content.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf-8 content: {}".format(utf_content))
