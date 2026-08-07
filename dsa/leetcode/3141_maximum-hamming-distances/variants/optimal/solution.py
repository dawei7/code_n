from collections import deque
from typing import List


class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        size = 1 << m
        distance = [-1] * size
        queue = deque()

        for value in nums:
            if distance[value] == -1:
                distance[value] = 0
                queue.append(value)

        while queue:
            value = queue.popleft()
            for bit in range(m):
                neighbor = value ^ (1 << bit)
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[value] + 1
                    queue.append(neighbor)

        mask = size - 1
        return [m - distance[value ^ mask] for value in nums]
