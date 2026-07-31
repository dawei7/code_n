from collections import Counter
from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        state_count = 1 << 10
        infinity = len(nums) + 1
        costs = [infinity] * state_count
        costs[0] = 0

        for offset in range(k):
            frequencies = Counter()
            group_size = 0
            for index in range(offset, len(nums), k):
                frequencies[nums[index]] += 1
                group_size += 1
            change_everything = min(costs) + group_size
            next_costs = [change_everything] * state_count

            for previous_xor, previous_cost in enumerate(costs):
                for value, frequency in frequencies.items():
                    resulting_xor = previous_xor ^ value
                    candidate = previous_cost + group_size - frequency
                    if candidate < next_costs[resulting_xor]:
                        next_costs[resulting_xor] = candidate

            costs = next_costs

        return costs[0]
