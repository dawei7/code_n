from collections import defaultdict
from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        length = len(nums)
        positions: dict[int, list[int]] = defaultdict(list)
        for index, value in enumerate(nums):
            positions[value].append(index)

        closest = [-1] * length
        for same_value in positions.values():
            count = len(same_value)
            if count < 2:
                continue
            for offset, index in enumerate(same_value):
                previous_index = same_value[offset - 1]
                next_index = same_value[(offset + 1) % count]
                closest[index] = min(
                    (index - previous_index) % length,
                    (next_index - index) % length,
                )

        return [closest[query] for query in queries]
