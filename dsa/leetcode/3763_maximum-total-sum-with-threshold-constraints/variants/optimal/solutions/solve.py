from typing import List


def solve(nums: List[int], threshold: List[int]) -> int:
    count_by_threshold = [0] * (len(nums) + 1)
    sum_by_threshold = [0] * (len(nums) + 1)
    for value, release_step in zip(nums, threshold):
        count_by_threshold[release_step] += 1
        sum_by_threshold[release_step] += value
    available = 0
    released_sum = 0
    for step in range(1, len(nums) + 1):
        available += count_by_threshold[step]
        released_sum += sum_by_threshold[step]
        if available == 0:
            return released_sum
        available -= 1
    return released_sum
