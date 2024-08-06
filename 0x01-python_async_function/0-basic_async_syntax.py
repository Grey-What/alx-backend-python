#!/usr/bin/env python3
"""conatains a coroutine"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """returns a float"""
    await asyncio.sleep(random.uniform(0, max_delay))
    return random.uniform(0, max_delay)
