from collections import deque
from typing import List


class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        start = tuple(nums1)
        target = tuple(nums2)
        if start == target:
            return 0

        n = len(nums1)
        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            state, operations = queue.popleft()
            for left in range(n):
                for right in range(left + 1, n + 1):
                    block = state[left:right]
                    remaining = state[:left] + state[right:]
                    for position in range(len(remaining) + 1):
                        next_state = (
                            remaining[:position]
                            + block
                            + remaining[position:]
                        )
                        if next_state == target:
                            return operations + 1
                        if next_state not in seen:
                            seen.add(next_state)
                            queue.append((next_state, operations + 1))

        return -1
