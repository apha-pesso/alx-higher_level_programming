#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    num = len(sys.argv)
    option = ['+', '-', '*', '/']
    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if op in option:
        if op == '+':
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
            exit(0)
        elif op == '-':
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
            exit(0)
        elif op == '*':
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
            exit(0)
        elif op == '/':
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
            exit(0)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
