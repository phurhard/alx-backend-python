#!/usr/bin/env python3
"""Annotations"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """This scripts takes a string and int/float then returns
    the output as a tuple with first element
    as string and second element as float

    Keyword arguments:
    k,v -- k is the first element and str,
    while v is the second element and int/float
    Return: Returns the square of v as floats and k in a tuple
    """

    return (k, v ** 2)
