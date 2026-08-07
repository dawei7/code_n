from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        candidates = deque([(0, 0)])
        prefix_sum = 0
        best_length = len(nums) + 1

        for end, value in enumerate(nums, 1):
            prefix_sum += value

            while candidates and prefix_sum - candidates[0][1] >= k:
                start, _ = candidates.popleft()
                best_length = min(best_length, end - start)

            while candidates and candidates[-1][1] >= prefix_sum:
                candidates.pop()

            candidates.append((end, prefix_sum))

        return best_length if best_length <= len(nums) else -1
