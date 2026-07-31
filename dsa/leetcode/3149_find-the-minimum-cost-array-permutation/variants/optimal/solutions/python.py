from functools import cache
from typing import List


def solve(nums: List[int]) -> List[int]:
    n = len(nums)
    full_mask = (1 << n) - 1

    @cache
    def best(mask: int, last: int) -> int:
        if mask == full_mask:
            return abs(last - nums[0])

        answer = 10**18
        for nxt in range(1, n):
            bit = 1 << nxt
            if mask & bit:
                continue
            candidate = abs(last - nums[nxt]) + best(mask | bit, nxt)
            answer = min(answer, candidate)
        return answer

    permutation = [0]
    mask = 1
    last = 0

    while mask != full_mask:
        target = best(mask, last)
        for nxt in range(1, n):
            bit = 1 << nxt
            if mask & bit:
                continue
            candidate = abs(last - nums[nxt]) + best(mask | bit, nxt)
            if candidate == target:
                permutation.append(nxt)
                mask |= bit
                last = nxt
                break

    return permutation
