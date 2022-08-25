#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num <= 1:
        print("0 arguments.")
        exit()
    elif num == 2:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1]))
        exit()
    else:
        print("{} arguments:".format(num - 1))
        for i in range(1, num):
            print("{}: {}".format(i, sys.argv[i]))
        exit()
