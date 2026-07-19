from typing import List


class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        length = len(nums)
        infinity = float("inf")
        previous = [infinity] * (length + 1)
        previous[0] = 0

        for groups in range(1, k + 2):
            current = [infinity] * (length + 1)

            for end in range(groups, length + 1):
                maximum = 0
                total = 0

                for start in range(end - 1, groups - 2, -1):
                    maximum = max(maximum, nums[start])
                    total += nums[start]
                    waste = maximum * (end - start) - total
                    current[end] = min(
                        current[end],
                        previous[start] + waste,
                    )

            previous = current

        return previous[length]
