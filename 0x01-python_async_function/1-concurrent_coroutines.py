#!/usr/bin/env python3
"""this module execute multiple coroutines
    at the same time with async
"""
import asyncio
from typing import List
wait_random =  __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ this function spawn wait_random """
    lst_task = [wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*lst_task)
    return delay
