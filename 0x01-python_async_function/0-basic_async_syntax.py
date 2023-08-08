#!/usr/bin/env python3
""" Asynchronous programming in python """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Returns the time spent in delaying the asynchronous progrsm"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
