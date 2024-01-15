#!/usr/bin/env python3
"""this module execute multiple coroutines
    at the same time with async
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ this function spawn wait_random """
    lst_task = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]
    delay = await asyncio.gather(*lst_task)
    return sorted(delay)
