#!/usr/bin/env python3
"""Annotation module"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """this function check element lenght"""
    return [(i, len(i)) for i in lst]
