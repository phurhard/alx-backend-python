#!/usr/bin/env python3
"""Annotation"""
import typing


def zoom_array(lst: typing.Tuple, factor: int = 2) -> typing.List:
    """Documentation for advanced annotations"""
    zoomed_in: typing.List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: typing.Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
