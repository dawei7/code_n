from typing import List


def solve(amount: List[int]) -> int:
    total = sum(amount)
    return max(max(amount), (total + 1) // 2)
