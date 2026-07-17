from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbors = defaultdict(list)
        for left, right in adjacentPairs:
            neighbors[left].append(right)
            neighbors[right].append(left)

        current = next(
            value for value, adjacent in neighbors.items() if len(adjacent) == 1
        )
        restored = [current]
        previous = None

        while len(restored) < len(neighbors):
            for candidate in neighbors[current]:
                if candidate != previous:
                    restored.append(candidate)
                    previous, current = current, candidate
                    break

        return restored
