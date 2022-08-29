#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == []:
        return
    for a in matrix:
        for i in a:
            print("{:d}".format(i), end=" ")
        print()
