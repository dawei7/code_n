from typing import List


def solve(nums: List[int], queries: List[List[int]]) -> List[bool]:
    violations = [0] * len(nums)
    for i in range(1, len(nums)):
        violations[i] = violations[i - 1] + int(nums[i] % 2 == nums[i - 1] % 2)
    return [violations[right] == violations[left] for left, right in queries]
