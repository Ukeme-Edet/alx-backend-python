#!/usr/bin/env python3
"""
Type Checking
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list that is a zoomed-in version of the input list

    Args:
        lst (Tuple): A tuple of integers
        factor (int): The factor by which to zoom the list

    Returns:
        List: A list that is a zoomed-in version of the input list
    """
    zoomed_in: list = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
