from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        blocked = {
            front
            for front, back in zip(fronts, backs)
            if front == back
        }

        smallest = None
        for front, back in zip(fronts, backs):
            if front not in blocked and (smallest is None or front < smallest):
                smallest = front
            if back not in blocked and (smallest is None or back < smallest):
                smallest = back

        return 0 if smallest is None else smallest
