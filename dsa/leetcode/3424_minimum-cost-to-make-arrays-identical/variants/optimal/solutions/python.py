from typing import List


def solve(arr: List[int], brr: List[int], k: int) -> int:
    cost_without_rearranging = sum(abs(a - b) for a, b in zip(arr, brr))
    cost_with_rearranging = k + sum(
        abs(a - b) for a, b in zip(sorted(arr), sorted(brr))
    )
    return min(cost_without_rearranging, cost_with_rearranging)
