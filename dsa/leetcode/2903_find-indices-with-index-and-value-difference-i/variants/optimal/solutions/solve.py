from typing import List


def solve(
    nums: List[int],
    indexDifference: int,
    valueDifference: int,
) -> List[int]:
    minimum_index = 0
    maximum_index = 0

    for right in range(indexDifference, len(nums)):
        candidate = right - indexDifference
        if nums[candidate] < nums[minimum_index]:
            minimum_index = candidate
        if nums[candidate] > nums[maximum_index]:
            maximum_index = candidate

        if nums[right] - nums[minimum_index] >= valueDifference:
            return [minimum_index, right]
        if nums[maximum_index] - nums[right] >= valueDifference:
            return [maximum_index, right]

    return [-1, -1]
