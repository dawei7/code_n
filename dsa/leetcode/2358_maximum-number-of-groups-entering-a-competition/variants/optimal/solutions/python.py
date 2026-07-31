from math import isqrt
from typing import List


def solve(grades: List[int]) -> int:
    return (isqrt(8 * len(grades) + 1) - 1) // 2
