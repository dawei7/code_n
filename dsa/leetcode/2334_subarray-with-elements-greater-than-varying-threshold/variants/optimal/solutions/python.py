from typing import List


def solve(nums: List[int], threshold: int) -> int:
    stack: List[int] = []

    for right in range(len(nums) + 1):
        value = nums[right] if right < len(nums) else -1
        while stack and nums[stack[-1]] > value:
            minimum = nums[stack.pop()]
            left = stack[-1] if stack else -1
            length = right - left - 1
            if minimum * length > threshold:
                return length
        stack.append(right)

    return -1
