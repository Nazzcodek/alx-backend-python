#!/usr/bin/env python3
"""this module measure async comprehension runtime"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """this methode mesaures the runtime of async comp"""
    start_time = time.perf_counter()
    asyncio.gather(*[async_comprehension() for _ in range(4)])
    total_time = time.perf_counter() - start_time
    return total_time
