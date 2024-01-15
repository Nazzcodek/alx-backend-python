#!/usr/bin/env python3
"""this is the task module"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """thsi function returns an asyncio task"""
    loop = asyncio.get_event_loop()
    task = asyncio.create_task(wait_random(max_delay))

    return task
