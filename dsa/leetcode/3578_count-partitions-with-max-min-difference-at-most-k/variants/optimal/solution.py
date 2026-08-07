from collections import deque
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        min_queue = deque()
        max_queue = deque()
        left = 0

        ways = [0] * (n + 1)
        prefix = [0] * (n + 2)
        ways[0] = 1
        prefix[1] = 1

        for right, value in enumerate(nums):
            while min_queue and nums[min_queue[-1]] >= value:
                min_queue.pop()
            min_queue.append(right)

            while max_queue and nums[max_queue[-1]] <= value:
                max_queue.pop()
            max_queue.append(right)

            while nums[max_queue[0]] - nums[min_queue[0]] > k:
                if min_queue[0] == left:
                    min_queue.popleft()
                if max_queue[0] == left:
                    max_queue.popleft()
                left += 1

            ways[right + 1] = (prefix[right + 1] - prefix[left]) % MOD
            prefix[right + 2] = (prefix[right + 1] + ways[right + 1]) % MOD

        return ways[n]
