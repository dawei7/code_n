from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        current = nums

        while len(current) > 1:
            next_values = []
            for index in range(len(current) // 2):
                first = current[2 * index]
                second = current[2 * index + 1]
                if index % 2 == 0:
                    next_values.append(min(first, second))
                else:
                    next_values.append(max(first, second))
            current = next_values

        return current[0]
