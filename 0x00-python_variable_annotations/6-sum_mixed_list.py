#!/usr/bin/env python3
"""this is an annotated module for mix list"""
from typing import List


def sum_mixed_list(mxd_list: List[int | float]) -> float:
    """this function returned the float of the sum"""
    return sum(float(mxd_list))
