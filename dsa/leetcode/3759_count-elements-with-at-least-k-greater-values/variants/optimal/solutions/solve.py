import random
from typing import List


def solve(nums: List[int], k: int) -> int:
    if k == 0:
        return len(nums)
    values = nums[:]
    target = len(values) - k
    left = 0
    right = len(values) - 1
    while left <= right:
        pivot = values[random.randint(left, right)]
        lower = left
        current = left
        upper = right
        while current <= upper:
            if values[current] < pivot:
                values[lower], values[current] = (values[current], values[lower])
                lower += 1
                current += 1
            elif values[current] > pivot:
                values[current], values[upper] = (values[upper], values[current])
                upper -= 1
            else:
                current += 1
        if target < lower:
            right = lower - 1
        elif target > upper:
            left = upper + 1
        else:
            threshold = pivot
            break
    return sum((value < threshold for value in nums))
