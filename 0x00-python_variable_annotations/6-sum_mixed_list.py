#!/usr/bin/env python3
"""Annotations"""
import typing


def sum_mixed_list(mxd_lst: typing.List[int | float]) -> float:
    """This script takes a list of mixed values and return the sum as a float

    Keyword arguments:
    mxd_lst -- input list
    sum -- sum of the list
    Return: Returns the sum as a float
    """

    sum: float = 0.0
    for flt in mxd_lst:
        sum += flt

    return sum
