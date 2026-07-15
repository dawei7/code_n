from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        frequencies = [0] * 101
        for height in heights:
            frequencies[height] += 1

        mismatches = 0
        position = 0
        for expected_height, frequency in enumerate(frequencies):
            for _ in range(frequency):
                if heights[position] != expected_height:
                    mismatches += 1
                position += 1

        return mismatches

