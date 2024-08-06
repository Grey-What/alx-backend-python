#!/usr/bin/env python3
"""module contains a coroutine"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    executes wait_random coroutine n times and
    returns a lsit of delays
    """
    delays = []
    for x in range(n):
        delays.append(await wait_random(max_delay))
    return delays
