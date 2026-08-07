from collections import defaultdict
from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        neighbors = defaultdict(set)
        for first, second in pairs:
            neighbors[first].add(second)
            neighbors[second].add(first)

        node_count = len(neighbors)
        root = next(
            (node for node, adjacent in neighbors.items() if len(adjacent) == node_count - 1),
            None,
        )
        if root is None:
            return 0

        result = 1
        for node, adjacent in neighbors.items():
            if node == root:
                continue

            parent = None
            parent_degree = node_count
            for candidate in adjacent:
                candidate_degree = len(neighbors[candidate])
                if len(adjacent) <= candidate_degree < parent_degree:
                    parent = candidate
                    parent_degree = candidate_degree

            if parent is None:
                return 0
            for neighbor in adjacent:
                if neighbor != parent and neighbor not in neighbors[parent]:
                    return 0
            if parent_degree == len(adjacent):
                result = 2

        return result
