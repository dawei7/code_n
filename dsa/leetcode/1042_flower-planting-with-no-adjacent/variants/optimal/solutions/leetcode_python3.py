from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        neighbors = [[] for _ in range(n)]
        for first, second in paths:
            first -= 1
            second -= 1
            neighbors[first].append(second)
            neighbors[second].append(first)

        flowers = [0] * n
        for garden in range(n):
            unavailable = {flowers[neighbor] for neighbor in neighbors[garden]}
            for flower_type in range(1, 5):
                if flower_type not in unavailable:
                    flowers[garden] = flower_type
                    break

        return flowers

