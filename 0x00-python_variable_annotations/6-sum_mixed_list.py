#!/usr/bin/env python3
"""module contains a type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of a list of floats and integers"""
    return sum(mxd_lst)
