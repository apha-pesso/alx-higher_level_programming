#!/usr/python3


def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))

    except (ValueError, ZeroDivisionError):
        print("Inside result: None")
        result = None

    finally:
        return result
