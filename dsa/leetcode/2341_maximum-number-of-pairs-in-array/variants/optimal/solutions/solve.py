from typing import List


def solve(nums: List[int]) -> List[int]:
    counts = [0] * 101
    for value in nums:
        counts[value] += 1

    pairs = sum(count // 2 for count in counts)
    return [pairs, len(nums) - 2 * pairs]
