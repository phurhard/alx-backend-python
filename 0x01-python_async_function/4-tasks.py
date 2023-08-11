#!/usr/bin/env python3
""" Asynchronous programming"""
import random
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


def bubble_sort(arr):
    """Sorts a list using bublle sort"""
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Returns a list of delays in the program"""
    ls = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay),  range(n)))
    )
    return sorted(ls)
