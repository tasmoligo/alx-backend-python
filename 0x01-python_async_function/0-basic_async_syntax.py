#!/usr/bin/env python3
"""
0-basic_async_syntax.py
"""
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.
    """
    number = random.uniform(0, max_delay + 1)
    return number
