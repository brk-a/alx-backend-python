#!/usr/bin/env python3

'''
Annotate the below function’s parameters and
return values with the appropriate types
'''

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Demostrates duck-typing """
    return [(i, len(i)) for i in lst]


if __name__ =='__main__':
    element_length =  __import__('9-element_length').element_length

    print(element_length.__annotations__)
