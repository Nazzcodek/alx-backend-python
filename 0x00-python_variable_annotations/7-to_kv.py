#!/usr/bin/env python3
"""this module is for tuple annotation"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ this function returns a tuple"""
    return (k, v**2)
