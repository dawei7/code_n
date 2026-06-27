from typing import List

def solve(nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                return [i, j]
    return [-1, -1]
