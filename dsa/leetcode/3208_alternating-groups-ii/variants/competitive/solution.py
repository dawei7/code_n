from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        size = len(colors)
        alternating_length = 1
        groups = 0
        for end in range(1, size + k - 1):
            if colors[end % size] != colors[(end - 1) % size]:
                alternating_length += 1
            else:
                alternating_length = 1
            if end >= k - 1 and alternating_length >= k:
                groups += 1
        return groups
