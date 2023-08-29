#!/usr/bin/env python3
"""a type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of the elements in the mixed list mxd_lst.
    """
    return sum(mxd_lst)
