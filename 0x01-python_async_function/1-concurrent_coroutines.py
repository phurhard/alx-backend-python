#!/usr/bin/env python3
""" Asynchronous programming"""
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


def bubble_sort(arr):
    """Sorts a list using bublle sort"""
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Returns a list of delays in the program"""
    ls = []
    while n:
        t = await wait_random(max_delay)
        n -= 1
        ls.append(t)
    bubble_sort(ls)

    return ls
