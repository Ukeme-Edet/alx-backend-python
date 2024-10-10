#!/usr/bin/env python3
"""
1-concat.py: Write a type-annotated function concat that takes a string str1\
    and a string str2 as arguments and returns a concatenated string.
"""


def concat(str1: str, str2: str) -> str:
    """
    Function that takes two arguments, both strings, and returns their\
        concatenation.

    Args:
        str1 (str): First string to concatenate.
        str2 (str): Second string to concatenate.

    Returns:
        str: The concatenation of str1 and str2.
    """
    return str1 + str2
