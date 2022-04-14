#!/usr/bin/env python3

'''
Defines a function that takes a float multiplier as an argument and
returns a function that multiplies a float by multiplier.
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a multiplier"""
    return (lambda x: x * multiplier)


if __name__ == '__main__':
    make_multiplier = __import__('8-make_multiplier').make_multiplier
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
