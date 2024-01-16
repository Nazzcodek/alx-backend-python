#!/usr/bin/env python3
"""this module use async comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """this is a methode for async comprehension"""
    result = [i async for i in async_generator()]
    return result
