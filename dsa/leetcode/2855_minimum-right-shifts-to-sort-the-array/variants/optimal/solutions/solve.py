from typing import List


def solve(nums: List[int]) -> int:
    n = len(nums)
    break_index = -1

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            if break_index != -1:
                return -1
            break_index = i

    if break_index == -1:
        return 0
    if nums[-1] > nums[0]:
        return -1
    return n - break_index - 1
