from collections import Counter
from functools import lru_cache


def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    group_size = n // k
    if max(Counter(nums).values()) > k:
        return -1

    group_cost = [-1] * (1 << n)
    for mask in range(1 << n):
        if mask.bit_count() != group_size:
            continue
        values = [nums[index] for index in range(n) if mask >> index & 1]
        if len(set(values)) != group_size:
            continue
        group_cost[mask] = max(values) - min(values)

    full_mask = (1 << n) - 1

    @lru_cache(None)
    def best(used_mask: int) -> int:
        if used_mask == full_mask:
            return 0

        remaining = full_mask ^ used_mask
        anchor = remaining & -remaining
        answer = float("inf")
        group_mask = remaining
        while group_mask:
            cost = group_cost[group_mask]
            if group_mask & anchor and cost >= 0:
                answer = min(answer, cost + best(used_mask | group_mask))
            group_mask = (group_mask - 1) & remaining
        return answer

    result = best(0)
    return -1 if result == float("inf") else int(result)
