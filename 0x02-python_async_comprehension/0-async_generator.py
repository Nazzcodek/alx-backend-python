#!/usr/bin/env python3
"""this is async comprehension genrator module"""
import asyncio
from random import uniform as u
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """this is async generator function"""
    for i in range(10):
        await asyncio.sleep(1)
        yield u(0, 10)
