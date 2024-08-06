#!/usr/bin/env python3
"""modules contains a function that returns a Task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a Task"""
    return asyncio.create_task(wait_random(max_delay))
