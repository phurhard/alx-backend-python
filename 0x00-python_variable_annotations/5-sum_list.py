#!/usr/bin/env python3
"""Annotations"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """This script defines a function sum_list and
    takes a list as input, it returns the sum of the floats in the list

    Keyword arguments:
    input_list -- A list of float values
    Return: returns the sum  of all floats in the list
    """
    sum: float = 0.0
    for flt in input_list:
        sum += flt
    return sum
