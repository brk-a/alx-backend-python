#!/usr/bin/env python3

'''
Defines a type annotated functions that concatenates 2 strings
'''


def concat(str1: str, str2: str) -> str:
    """returns concatenated string"""
    return str1 + str2


if __name__ == '__main__':
    concat = __import__('1-concat').concat

    str1 = "egg"
    str2 = "shell"

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
