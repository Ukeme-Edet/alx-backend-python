#!/usr/bin/env python3
"""
This module contains the function for task 6
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    Sums up a list of numbers

    Args:
        mxd_lst (List[int | float]): The list of numbers to be summed

    Returns:
        float: The sum of the numbers
    """
    return sum(float(x) for x in mxd_lst)
