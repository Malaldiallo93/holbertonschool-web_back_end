#!/usr/bin/env python3
"""Coroutine called measure_runtime using that
execute async_comprehension four times"""
import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel"""

    start_time = time.time()
    """Four times in parallel"""
    list_coroutines = [async_comprehension() for i in range(4)]
    """Unpack coroutines"""
    await asyncio.gather(*list_coroutines)
    end_time = time.time()

    total_runtime = end_time - start_time
    return total_runtime
