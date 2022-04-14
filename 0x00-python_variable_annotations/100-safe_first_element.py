#!/usr/bin/env python3

'''
Augment the following code with the correct duck-typed annotations
'''

from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns list element at 0 if list is not empty else returns None"""
    if not lst:
        return None
    return lst[0]

if __name__ == '__main__':
    safe_first_element =  __import__\
        ('100-safe_first_element').safe_first_element

    print(safe_first_element.__annotations__)
