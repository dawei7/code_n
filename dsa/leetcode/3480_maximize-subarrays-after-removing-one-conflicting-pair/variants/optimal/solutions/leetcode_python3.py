from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        by_right = [[] for _ in range(n + 1)]
        for pair_id, (first, second) in enumerate(conflictingPairs):
            left, right = sorted((first, second))
            by_right[right].append((left, pair_id))

        largest_left = 0
        second_largest_left = 0
        largest_pair_id = -1
        valid_subarrays = 0
        removal_gain = [0] * len(conflictingPairs)

        for right in range(1, n + 1):
            for left, pair_id in by_right[right]:
                if left > largest_left:
                    second_largest_left = largest_left
                    largest_left = left
                    largest_pair_id = pair_id
                elif left > second_largest_left:
                    second_largest_left = left

            valid_subarrays += right - largest_left
            if largest_pair_id != -1:
                removal_gain[largest_pair_id] += (
                    largest_left - second_largest_left
                )

        return valid_subarrays + max(removal_gain)
