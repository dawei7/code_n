from typing import List


def solve(nums: List[int], k: int) -> int:
    answer = 0
    window_sum = 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum * (right - left + 1) >= k:
            window_sum -= nums[left]
            left += 1
        answer += right - left + 1
    return answer
