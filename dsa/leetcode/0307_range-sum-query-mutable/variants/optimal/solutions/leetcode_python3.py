class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums[:]
        self.bit = [0] * (len(nums) + 1)
        for index, value in enumerate(nums):
            self._add(index, value)

    def _add(self, index: int, delta: int) -> None:
        index += 1
        while index < len(self.bit):
            self.bit[index] += delta
            index += index & -index

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index, delta)

    def _prefix_sum(self, index: int) -> int:
        total = 0
        index += 1
        while index > 0:
            total += self.bit[index]
            index -= index & -index
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right) - self._prefix_sum(left - 1)
