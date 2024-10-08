#!/usr/bin/env python3
"""module contains a type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    return lambda x: x * multiplier
