#!/usr/bin/env python3

'''
Defines a function that takes in a mixed list of integers and
floats and returns their sum as a float.
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of integers and floats and returns the sum"""
    return sum(mxd_lst)


if __name__ == '__main__':
    sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

    print(sum_mixed_list.__annotations__)
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}".format\
          (ans, type(ans)))
