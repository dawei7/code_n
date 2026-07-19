from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weights = sorted(people)
        light = 0
        heavy = len(weights) - 1
        boats = 0

        while light <= heavy:
            if weights[light] + weights[heavy] <= limit:
                light += 1
            heavy -= 1
            boats += 1

        return boats
