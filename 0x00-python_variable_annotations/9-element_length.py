#!/usr/bin/env python3
"""module contains a type-annotated function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of tuples"""
    return [(i, len(i)) for i in lst]
