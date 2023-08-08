#!/usr/bin/env python3
"""Asynchronous programming"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measured the total time for the execution of wait_n"""
    start = time.perf_counter()
    t = await wait_n(n, max_delay)
    end = time.perf_counter() - start
    return end / n
