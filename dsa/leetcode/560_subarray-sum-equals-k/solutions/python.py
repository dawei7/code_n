"""Prefix-sum frequency counting for LeetCode 560."""


def solve(nums: list[int], k: int) -> int:
    prefix_frequency = {0: 1}
    prefix = 0
    answer = 0

    for value in nums:
        prefix += value
        answer += prefix_frequency.get(prefix - k, 0)
        prefix_frequency[prefix] = prefix_frequency.get(prefix, 0) + 1

    return answer

