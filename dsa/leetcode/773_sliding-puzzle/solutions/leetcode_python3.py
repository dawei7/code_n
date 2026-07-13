from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = "".join(str(value) for row in board for value in row)
        target = "123450"
        neighbors = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            state, distance = queue.popleft()
            if state == target:
                return distance
            blank = state.index("0")
            for adjacent in neighbors[blank]:
                candidate = list(state)
                candidate[blank], candidate[adjacent] = candidate[adjacent], candidate[blank]
                next_state = "".join(candidate)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, distance + 1))
        return -1
