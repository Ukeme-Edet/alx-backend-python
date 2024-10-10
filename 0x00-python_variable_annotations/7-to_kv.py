#!/usr/bin/env python3
"""
This module contains the function for task 7
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key and a value to a tuple where the key is a string and the\
        value is the square of the original value.

    Args:
        k (str): The key.
        v (Union[int, float]): The value to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.
    """
    return (k, v**0.5)
