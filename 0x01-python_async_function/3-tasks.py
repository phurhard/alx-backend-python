#!/usr/bin/env python3
"""Asynchronous programmig"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns asyncio.Task"""
    wait = asyncio.create_task(wait_random())
    return wait
