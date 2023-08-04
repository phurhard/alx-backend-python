#!/usr/bin/env python3
"""Annotations"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """This script is a function that returns a function that multiplies
    a float by the multiplier

    Keyword arguments:
    multiplier -- input to the function
    Return: returns a function that can be used to multiply
    """

    def multiply(a):
        mul = a * multiplier
        return mul

    return multiply
