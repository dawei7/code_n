from typing import List


class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        alive = FenwickTree(n)
        for index in range(1, n + 1):
            alive.add(index, 1)

        operations = 0
        current = 0

        for target in sorted(range(n), key=nums.__getitem__):
            if target >= current:
                rotations = alive.prefix_sum(target) - alive.prefix_sum(current)
            else:
                rotations = (
                    alive.prefix_sum(n)
                    - alive.prefix_sum(current)
                    + alive.prefix_sum(target)
                )

            operations += rotations + 1
            alive.add(target + 1, -1)
            current = target

        return operations
