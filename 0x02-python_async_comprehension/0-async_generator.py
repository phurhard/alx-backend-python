#!/usr/bin/env python3
"""Asynchronous Comprehension"""
import random
import asyncio


async def async_generator():
    """Asynchronous generator function"""
    for i in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
