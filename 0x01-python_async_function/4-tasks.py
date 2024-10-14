#!/usr/bin/env python3
"""
This module contains a function that creates an asyncio task.
"""
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a random delay between 0 and `max_delay` seconds.

    Args:
        n (int): The number of times to call `wait_random`.
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        List[float]: A list of random delays.
    """
    import asyncio

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
