#!/usr/bin/env python3
"""This module is for flaot mutiplier"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """it takes a float and multiply"""
    
    def multiply(fun: float) -> float:
        """fun function"""
        return fun * multiplier

    return multiply
