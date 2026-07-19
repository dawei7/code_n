from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        deadlines = sorted(
            (distance - 1) // monster_speed
            for distance, monster_speed in zip(dist, speed)
        )

        for minute, deadline in enumerate(deadlines):
            if deadline < minute:
                return minute

        return len(deadlines)
