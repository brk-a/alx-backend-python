#!/usr/bin/env python3

'''
Given the parameters and the return values,
add type annotations to the function
'''

from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Return a key if found in dict else return None """
    if key in dct:
        return dct[key]
    else:
        return default


    if __name__ == '__main__':
        safely_get_value = __import__('101-safely_get_value')\
            .safely_get_value
        annotations = safely_get_value.__annotations__

        print("Here's what the mappings should look like")
        for k, v in annotations.items():
            print( ("{}: {}".format(k, v)))
