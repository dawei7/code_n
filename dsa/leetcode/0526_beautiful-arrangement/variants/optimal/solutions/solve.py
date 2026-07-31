"""Memoized bitmask search for LeetCode 526."""

from functools import cache


def solve(n: int) -> int:
    full_mask = (1 << n) - 1

    @cache
    def count_completions(used_mask: int) -> int:
        if used_mask == full_mask:
            return 1

        position = used_mask.bit_count() + 1
        total = 0
        for value in range(1, n + 1):
            bit = 1 << (value - 1)
            if used_mask & bit:
                continue
            if value % position == 0 or position % value == 0:
                total += count_completions(used_mask | bit)
        return total

    return count_completions(0)
