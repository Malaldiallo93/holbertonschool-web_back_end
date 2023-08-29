#!/usr/bin/env python3
""" a type-annotated function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k as the first element and
    the square of the int/float v as the second element (annotated as a float).
    """
    return k, v ** 2
