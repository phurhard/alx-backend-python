#!/usr/bin/env python3
"""Asynchronous Comprehension"""
import random
import asyncio
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Asynchronous generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
