from typing import List


def solve(nums: List[int], k: int) -> int:
    left = 0
    window_sum = 0
    answer = 0

    for right, value in enumerate(nums):
        window_sum += value

        while window_sum * (right - left + 1) >= k:
            window_sum -= nums[left]
            left += 1

        answer += right - left + 1

    return answer
