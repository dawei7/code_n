from math import gcd
from typing import List


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        node_count = len(nums)
        adjacency = [[] for _ in range(node_count)]
        for first, second in edges:
            adjacency[first].append(second)
            adjacency[second].append(first)

        coprime_values = [[] for _ in range(51)]
        for value in range(1, 51):
            coprime_values[value] = [
                candidate
                for candidate in range(1, 51)
                if gcd(value, candidate) == 1
            ]

        active_by_value = [[] for _ in range(51)]
        answer = [-1] * node_count
        stack = [(0, -1, 0, False)]

        while stack:
            node, parent, depth, exiting = stack.pop()
            value = nums[node]

            if exiting:
                active_by_value[value].pop()
                continue

            best_depth = -1
            for candidate in coprime_values[value]:
                if (
                    active_by_value[candidate]
                    and active_by_value[candidate][-1][1] > best_depth
                ):
                    answer[node], best_depth = active_by_value[candidate][-1]

            active_by_value[value].append((node, depth))
            stack.append((node, parent, depth, True))
            for neighbor in reversed(adjacency[node]):
                if neighbor != parent:
                    stack.append((neighbor, node, depth + 1, False))

        return answer
