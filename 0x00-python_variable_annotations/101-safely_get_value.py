#!/usr/bin/env python3
"""
This module contains the function for task 101
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Returns the value of a key in a dictionary

    Args:
        dct (Mapping): a dictionary
        key (Any): a key
        default (Union[T, None]): a default value

    Returns:
        Union[Any, T]: the value of the key in the dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
