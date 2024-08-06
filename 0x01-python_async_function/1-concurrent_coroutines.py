#!/usr/bin/env python3
"""module contains a coroutine"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns a lsit of delays"""
    return [await wait_random(max_delay) for x in range(n)]
