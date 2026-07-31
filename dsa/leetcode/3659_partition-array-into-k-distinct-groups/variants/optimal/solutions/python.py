from collections import Counter


def solve(nums: list[int], k: int) -> bool:
    if len(nums) % k:
        return False

    group_count = len(nums) // k
    return max(Counter(nums).values()) <= group_count
