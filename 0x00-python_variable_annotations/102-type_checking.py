#!/usr/bin/env python3

'''
Use mypy to validate the following piece of
code and apply any necessary changes.
'''

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a List from a tuple"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

if __name__ == '__main__':
    zoom_array =  __import__('102-type_checking').zoom_array

    print(zoom_array.__annotations__)

    
