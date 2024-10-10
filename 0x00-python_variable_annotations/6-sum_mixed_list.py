#!/usr/bin/env python3
'''type-annotated function sum_mixed_list which takes
a list mxd_lst of integers and floats as argument
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the sum of the as a float'''
    result = 0
    for element in mxd_lst:
        result = result + element
    return result
