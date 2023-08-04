#!/usr/bin/env python3
"""Annotations"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) ->\
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """Returns the length of each element in a list

    Keyword arguments:
    lst -- the input list
    Return: a tuple of i and length of the element
    """

    return [(i, len(i)) for i in lst]
