#!/usr/bin/env python3
"""module contains a function that measures the runtime of coroutine"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    executes wait_n coroutine and measures the total runtime
    """
    now = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - now)
