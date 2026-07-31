from typing import List


def solve(nums: List[int]) -> int:
    answer = 0
    for value in nums:
        answer |= value
    return answer
