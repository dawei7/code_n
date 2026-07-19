from bisect import bisect_left
from itertools import combinations
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        left = nums[:n]
        right = nums[n:]
        right_sums = [
            sorted(sum(group) for group in combinations(right, count))
            for count in range(n + 1)
        ]

        total = sum(nums)
        answer = float("inf")

        for left_count in range(n + 1):
            compatible = right_sums[n - left_count]
            for group in combinations(left, left_count):
                left_sum = sum(group)
                target = total / 2 - left_sum
                index = bisect_left(compatible, target)

                for candidate_index in (index - 1, index):
                    if 0 <= candidate_index < len(compatible):
                        chosen_sum = left_sum + compatible[candidate_index]
                        answer = min(answer, abs(total - 2 * chosen_sum))

        return int(answer)
