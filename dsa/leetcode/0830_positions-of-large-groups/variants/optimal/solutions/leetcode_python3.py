from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        groups = []
        run_start = 0

        for end in range(1, len(s) + 1):
            if end < len(s) and s[end] == s[run_start]:
                continue
            if end - run_start >= 3:
                groups.append([run_start, end - 1])
            run_start = end

        return groups
