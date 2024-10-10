#!/usr/bin/env python3
"""
This module contains the function for task 100
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence

    Args:
        lst (Sequence[Any]): a sequence of elements

    Returns:
        Union[Any, None]: the first element of the sequence
    """
    if lst:
        return lst[0]
    else:
        return None
