from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        size = len(colors)
        return sum(
            colors[index] != colors[index - 1]
            and colors[index] != colors[(index + 1) % size]
            for index in range(size)
        )
