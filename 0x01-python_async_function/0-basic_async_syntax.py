#!/usr/bin/env python3
"""the basic of async"""

import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """this is an async function for max delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
