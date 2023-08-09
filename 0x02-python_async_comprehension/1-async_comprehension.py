#!/usr/bin/env python3
"""Asynchronous comprehension"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Asynchronous list comorehension"""
    return [i async for i in async_generator()]
