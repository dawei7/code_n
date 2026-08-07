from collections import deque
from typing import List


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        n = len(status)
        owned = [False] * n
        openable = [value == 1 for value in status]
        opened = [False] * n
        queue = deque()

        for box in initialBoxes:
            owned[box] = True
            if openable[box]:
                queue.append(box)

        total = 0
        while queue:
            box = queue.popleft()
            if opened[box] or not owned[box] or not openable[box]:
                continue

            opened[box] = True
            total += candies[box]

            for key in keys[box]:
                openable[key] = True
                if owned[key] and not opened[key]:
                    queue.append(key)

            for child in containedBoxes[box]:
                owned[child] = True
                if openable[child] and not opened[child]:
                    queue.append(child)

        return total
