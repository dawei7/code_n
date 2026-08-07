from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        modulus = 1_000_000_007
        ways = [1] * (nums[0] + 1)

        for previous_value, current_value in zip(nums, nums[1:]):
            prefix = []
            running_sum = 0
            for count in ways:
                running_sum = (running_sum + count) % modulus
                prefix.append(running_sum)

            minimum_increase = max(0, current_value - previous_value)
            next_ways = [0] * (current_value + 1)
            for current_first in range(minimum_increase, current_value + 1):
                previous_limit = current_first - minimum_increase
                if previous_limit < len(prefix):
                    next_ways[current_first] = prefix[previous_limit]
                else:
                    next_ways[current_first] = prefix[-1]
            ways = next_ways

        return sum(ways) % modulus
