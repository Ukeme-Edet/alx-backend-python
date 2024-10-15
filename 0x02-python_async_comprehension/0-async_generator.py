#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async Generator

    Args:
        None

    Returns:
        AsyncGenerator[float, None]: An async generator that yields a random\
            float
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
