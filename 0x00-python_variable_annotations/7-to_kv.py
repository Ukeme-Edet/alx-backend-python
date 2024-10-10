#!/usr/bin/env python3
"""
This module contains the function for task 7
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of a string and the sqrt of v

    Args:
        k (str): The string k
        v: (Union[int, float]): The number to be rooted

    Returns:
        Tuple[str, float]: A tuple of the string and rooted number
    """
    return (k, v**0.5)
