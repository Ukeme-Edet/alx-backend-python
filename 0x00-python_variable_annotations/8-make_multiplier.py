#!/usr/bin/env python3
"""
This module contains a function that creates a multiplier function.

The `make_multiplier` function takes a float `multiplier` as an argument
and returns a function that multiplies its input by the given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier - Returns a function that multiplies a given float by a\
        specified multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns\
            the product of it and the multiplier.
    """
    return lambda x: x * multiplier
