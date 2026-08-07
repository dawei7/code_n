from collections import deque
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        candidates = deque()
        answer = nums[0]
        for index, value in enumerate(nums):
            while candidates and candidates[0][0] < index - k:
                candidates.popleft()
            ending_sum = value + max(0, candidates[0][1] if candidates else 0)
            answer = max(answer, ending_sum)
            while candidates and candidates[-1][1] <= ending_sum:
                candidates.pop()
            candidates.append((index, ending_sum))
        return answer
