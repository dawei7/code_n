from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        positions = defaultdict(list)
        for index, value in enumerate(arr):
            positions[value].append(index)

        queue = deque([(0, 0)])
        seen = {0}
        while queue:
            index, jumps = queue.popleft()
            destinations = positions.pop(arr[index], ())
            for next_index in (*destinations, index - 1, index + 1):
                if next_index == len(arr) - 1:
                    return jumps + 1
                if 0 <= next_index < len(arr) and next_index not in seen:
                    seen.add(next_index)
                    queue.append((next_index, jumps + 1))

        return -1
