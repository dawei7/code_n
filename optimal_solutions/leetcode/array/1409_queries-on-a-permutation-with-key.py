"""Optimal solution for LeetCode 1409: Queries on a Permutation With Key."""


class _Fenwick:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def sum(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


def solve(queries: list[int], m: int) -> list[int]:
    q = len(queries)
    bit = _Fenwick(q + m + 2)
    positions = {value: q + value for value in range(1, m + 1)}
    for pos in positions.values():
        bit.add(pos, 1)

    answer: list[int] = []
    front = q
    for value in queries:
        pos = positions[value]
        answer.append(bit.sum(pos) - 1)
        bit.add(pos, -1)
        positions[value] = front
        bit.add(front, 1)
        front -= 1
    return answer
