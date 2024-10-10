#!/usr/bin/env python3
'''type-annotated function sum_list which takes
a list input_list of floats as argument
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Returns the sum of the arary'''
    result = 0
    for element in input_list:
        result = result + element
    return result
