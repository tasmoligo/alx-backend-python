#!/usr/bin/env python3
"""
4-tasks.py
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn task_wait_random n times with the specified max_delay
    """
    number_list = []
    delays = []
    for i in range(n):
        number = task_wait_random(max_delay)
        number_list.append(number)
    for number in asyncio.as_completed((number_list)):
        delay = await number
        delays.append(delay)
    return delays
