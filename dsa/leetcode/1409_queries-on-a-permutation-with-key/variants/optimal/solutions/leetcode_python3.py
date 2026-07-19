from typing import List


class Fenwick:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    def add(self, index, delta):
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index
    def prefix_sum(self, index):
        total = 0
        while index:
            total += self.tree[index]
            index -= index & -index
        return total


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        q = len(queries)
        tree = Fenwick(q + m + 1)
        positions = [0] * (m + 1)
        for value in range(1, m + 1):
            positions[value] = q + value
            tree.add(positions[value], 1)
        answer = []
        front = q
        for value in queries:
            position = positions[value]
            answer.append(tree.prefix_sum(position) - 1)
            tree.add(position, -1)
            positions[value] = front
            tree.add(front, 1)
            front -= 1
        return answer
