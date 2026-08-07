from typing import List


_LIMIT = 1_000_000
_SMALLEST_FACTOR = [0] * (_LIMIT + 1)
for _factor in range(2, 1001):
    if _SMALLEST_FACTOR[_factor] != 0:
        continue
    for _multiple in range(_factor * _factor, _LIMIT + 1, _factor):
        if _SMALLEST_FACTOR[_multiple] == 0:
            _SMALLEST_FACTOR[_multiple] = _factor


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        values = nums[:]
        operations = 0

        for index in range(len(values) - 2, -1, -1):
            if values[index] <= values[index + 1]:
                continue

            factor = _SMALLEST_FACTOR[values[index]]
            if factor == 0 or factor > values[index + 1]:
                return -1

            values[index] = factor
            operations += 1

        return operations
