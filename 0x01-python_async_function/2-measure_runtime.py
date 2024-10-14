#!/usr/bin/env python3
"""
This module contains a function that measures the runtime of an async coroutine.
"""
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the runtime of `wait_n` called `n` times with `max_delay`.

    Args:
        n (int): The number of times to call `wait_n`.
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        float: The average runtime.
    """
    import time
    import asyncio

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
