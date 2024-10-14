#!/usr/bin/env python3
"""
This module contains a function that creates an asyncio task.
"""
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Asynchronously waits for a random delay between 0 and `max_delay` seconds.

    Args:
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        float: The random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
