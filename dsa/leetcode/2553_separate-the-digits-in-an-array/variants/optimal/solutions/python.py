from typing import List


def solve(nums: List[int]) -> List[int]:
    return [
        int(digit)
        for number in nums
        for digit in str(number)
    ]
