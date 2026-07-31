from typing import List


def solve(nums: List[int], k: int) -> int:
    frequencies = [0] * 31
    for value in set(nums):
        frequencies[value.bit_count()] += 1

    answer = 0
    for first_count, first_frequency in enumerate(frequencies):
        for second_count, second_frequency in enumerate(frequencies):
            if first_count + second_count >= k:
                answer += first_frequency * second_frequency
    return answer
