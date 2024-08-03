#!/usr/bin/env python3
"""agumenting code with correct duck-typed annotations"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
