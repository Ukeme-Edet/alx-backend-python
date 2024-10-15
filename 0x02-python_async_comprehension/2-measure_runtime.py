#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime

    Args:
        None

    Returns:
        float: The runtime
    """
    import time

    start = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.time()
    return end - start
