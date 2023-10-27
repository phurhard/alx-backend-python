#!/usr/bin/env python3
"""Annotations"""
import typing


# The types of the elements of the input are not know
def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing.Union[None, typing.Any]:
    """Advanced tired"""
    return lst[0] if lst else None
