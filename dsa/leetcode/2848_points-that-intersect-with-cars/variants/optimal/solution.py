from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        difference = [0] * 102
        for start, end in nums:
            difference[start] += 1
            difference[end + 1] -= 1

        covered = 0
        active = 0
        for point in range(1, 101):
            active += difference[point]
            covered += active > 0
        return covered
