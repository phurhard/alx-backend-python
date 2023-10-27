#!/usr/bin/env python3
"""Annotations advance"""
import typing
T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any,
                     default: typing.Union[T, None] = None) -> typing.Union[typing.Any, T]:
    """Documentation for advanced annotations"""
    return dct[key] if key in dct else default
