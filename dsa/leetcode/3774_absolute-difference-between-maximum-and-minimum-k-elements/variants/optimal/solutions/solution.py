from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        frequency = [0] * 101
        for value in nums:
            frequency[value] += 1

        smallest_sum = 0
        remaining = k
        for value in range(1, 101):
            taken = min(remaining, frequency[value])
            smallest_sum += taken * value
            remaining -= taken
            if remaining == 0:
                break

        largest_sum = 0
        remaining = k
        for value in range(100, 0, -1):
            taken = min(remaining, frequency[value])
            largest_sum += taken * value
            remaining -= taken
            if remaining == 0:
                break

        return abs(largest_sum - smallest_sum)
