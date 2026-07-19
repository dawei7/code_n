from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        water = capacity

        for index, requirement in enumerate(plants):
            if water < requirement:
                steps += 2 * index
                water = capacity

            steps += 1
            water -= requirement

        return steps
