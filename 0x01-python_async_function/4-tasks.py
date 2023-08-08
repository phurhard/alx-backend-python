#!/usr/bin/env python3
""" Asynchronous programming"""
import random
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Returns a list of delays in the program"""
    ls = []
    while n:
        t = await task_wait_random(max_delay)
        n -= 1
        ls.append(t)
    return ls
