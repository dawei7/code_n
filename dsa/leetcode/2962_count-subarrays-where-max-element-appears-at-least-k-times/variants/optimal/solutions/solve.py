from typing import List


def solve(nums: List[int], k: int) -> int:
    maximum = max(nums)
    left = 0
    maximum_count = 0
    answer = 0

    for value in nums:
        if value == maximum:
            maximum_count += 1
        while maximum_count >= k:
            if nums[left] == maximum:
                maximum_count -= 1
            left += 1
        answer += left

    return answer
