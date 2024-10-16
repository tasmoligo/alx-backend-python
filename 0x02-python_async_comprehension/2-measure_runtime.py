#!/usr/bin/env python3
"""
1-async_comprehension.py
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel
    and measure the total runtime and return it.
    """
    startTime = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    endTime = time.time()
    return endTime - startTime
