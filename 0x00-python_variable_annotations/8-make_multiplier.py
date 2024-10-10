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

    def multiply(n: float) -> float:
        """
        multiply - Multiplies a given float by the multiplier.

        Args:
            n (float): The number to multiply.

        Returns:
            float: The product of the input number and the multiplier.
        """
        return n * multiplier

    return multiply
