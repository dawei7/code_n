from typing import List


def solve(nums: List[int]) -> int:
    largest = [-1] * 82
    answer = -1

    for value in nums:
        remaining = value
        digit_sum = 0
        while remaining:
            digit_sum += remaining % 10
            remaining //= 10

        if largest[digit_sum] != -1:
            answer = max(answer, largest[digit_sum] + value)
        largest[digit_sum] = max(largest[digit_sum], value)

    return answer
