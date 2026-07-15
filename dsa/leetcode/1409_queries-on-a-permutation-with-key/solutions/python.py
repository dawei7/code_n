"""Optimal app-local solution for LeetCode 1409."""


class _Fenwick:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index: int) -> int:
        total = 0
        while index:
            total += self.tree[index]
            index -= index & -index
        return total


def solve(queries: list[int], m: int) -> list[int]:
    query_count = len(queries)
    tree = _Fenwick(query_count + m + 1)
    positions = [0] * (m + 1)
    for value in range(1, m + 1):
        positions[value] = query_count + value
        tree.add(positions[value], 1)

    answer: list[int] = []
    front = query_count
    for value in queries:
        position = positions[value]
        answer.append(tree.prefix_sum(position) - 1)
        tree.add(position, -1)
        positions[value] = front
        tree.add(front, 1)
        front -= 1
    return answer
