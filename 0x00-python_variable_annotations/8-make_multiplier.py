#!/usr/bin/env python3
'''type-annotated function make_multiplier that takes a
float multiplier as argument
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies a float by multiplier.'''
    def return_function(arg: float) -> float:
        return multiplier * arg
    return return_function
