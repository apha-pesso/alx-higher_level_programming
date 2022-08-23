#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            print("{:c}".format(ord(str[i]) - 32), end="")
        else:
            print(str[i], end="")
    print()
