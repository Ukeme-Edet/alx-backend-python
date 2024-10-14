#!/usr/bin/env python3
"""
This module contains an async coroutine that waits for a random delay.
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and `max_delay` seconds.

    Args:
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        float: The random delay.
    """
    import asyncio
    import random

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
