"""Fenwick-tree solution for LeetCode 307."""


class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums[:]
        self.bit = [0] * (len(nums) + 1)
        for i, value in enumerate(nums):
            self._add(i, value)

    def _add(self, i: int, delta: int) -> None:
        i += 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i

    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        self.nums[i] = val
        self._add(i, delta)

    def _prefix_sum(self, i: int) -> int:
        total = 0
        i += 1
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right) - self._prefix_sum(left - 1)


def solve(arr: list[int], n: int, queries: list[list[int | str]], q: int) -> list[int]:
    num_array = NumArray(arr[:n])
    results = []
    for operation in queries[:q]:
        if operation[0] == "update":
            num_array.update(operation[1], operation[2])
        else:
            results.append(num_array.sumRange(operation[1], operation[2]))
    return results
