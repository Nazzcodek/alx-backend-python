#!/usr/bin/env python3
"""annotated module"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """the first safe element"""
    if lst:
        return lst[0]
    else:
        return None
