#!/usr/bin/env python3
"""a type-annotated function sum_list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of the elements in the input_list.
    """
    return sum(input_list)
