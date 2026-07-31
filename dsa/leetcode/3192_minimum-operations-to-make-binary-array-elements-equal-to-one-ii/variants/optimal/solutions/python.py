from typing import List


def solve(nums: List[int]) -> int:
    operations = 0
    flipped = 0

    for num in nums:
        if (num ^ flipped) == 0:
            operations += 1
            flipped ^= 1

    return operations
