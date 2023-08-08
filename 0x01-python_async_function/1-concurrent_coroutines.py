#!/usr/bin/env python3
""" Asynchronous programming"""
import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Returns a list of delays in the program"""
    ls = []
    while n:
        t = await wait_random(max_delay)
        n -= 1
        ls.append(t)
    return ls
