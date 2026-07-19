from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        best_score = [0] * len(nums)
        best_score[0] = nums[0]
        candidates = deque([0])

        for index in range(1, len(nums)):
            while candidates[0] < index - k:
                candidates.popleft()
            best_score[index] = nums[index] + best_score[candidates[0]]
            while candidates and best_score[candidates[-1]] <= best_score[index]:
                candidates.pop()
            candidates.append(index)

        return best_score[-1]
