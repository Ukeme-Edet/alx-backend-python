#!/usr/bin/env python3
"""
This module contains a function that takes an iterable of sequences and\
    returns a list of tuples,
where each tuple contains a sequence from the input and its corresponding\
    length.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in a list of sequences.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains\
            a sequence from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
