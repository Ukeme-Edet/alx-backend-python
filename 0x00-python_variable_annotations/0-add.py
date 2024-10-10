#!/usr/bin/env python3
"""
0-add.py: Write a type-annotated function add that takes a float a and a float
b as arguments and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """
    Function that takes two arguments a and b, both floats, and returns their\
        sum as a float.

    Args:
        a (float): First number to add.
        b (float): Second number to add.

    Returns:
        float: The sum of a and b.
    """
    return a + b
