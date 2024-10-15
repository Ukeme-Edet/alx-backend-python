#!/usr/bin/env python3
"""
Async Comprehensions
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Async Comprehensions

    Args:
        None

    Returns:
        List[float]: A list of 10 random floats
    """
    return [i async for i in async_generator()]
