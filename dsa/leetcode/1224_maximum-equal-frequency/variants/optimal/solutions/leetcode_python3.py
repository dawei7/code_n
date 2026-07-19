from collections import Counter
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counts = Counter()
        frequency_counts = Counter()
        answer = 0
        maximum_frequency = 0

        for length, value in enumerate(nums, 1):
            old_frequency = counts[value]
            if old_frequency:
                frequency_counts[old_frequency] -= 1
            counts[value] = old_frequency + 1
            frequency_counts[old_frequency + 1] += 1
            maximum_frequency = max(maximum_frequency, old_frequency + 1)

            if (
                maximum_frequency == 1
                or maximum_frequency * frequency_counts[maximum_frequency] + 1 == length
                or (maximum_frequency - 1)
                * (frequency_counts[maximum_frequency - 1] + 1)
                + 1
                == length
            ):
                answer = length
        return answer
