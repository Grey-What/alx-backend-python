#!/usr/bin/env python3
"""module contains a coroutine called async_generator"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """coroutine that takes no arguments that yields a random value"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
