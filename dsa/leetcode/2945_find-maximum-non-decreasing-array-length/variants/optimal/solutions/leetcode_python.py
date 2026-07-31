from collections import deque
from typing import List


class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        length = len(nums)
        prefix = [0] * (length + 1)
        groups = [0] * (length + 1)
        last_sum = [0] * (length + 1)
        candidates = deque([0])

        for end, value in enumerate(nums, start=1):
            prefix[end] = prefix[end - 1] + value

            while len(candidates) > 1 and prefix[candidates[1]] + last_sum[candidates[1]] <= prefix[end]:
                candidates.popleft()

            previous = candidates[0]
            groups[end] = groups[previous] + 1
            last_sum[end] = prefix[end] - prefix[previous]
            threshold = prefix[end] + last_sum[end]

            while candidates and prefix[candidates[-1]] + last_sum[candidates[-1]] >= threshold:
                candidates.pop()
            candidates.append(end)

        return groups[length]
