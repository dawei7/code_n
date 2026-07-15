from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        score = 0
        first_seen = {}
        best = 0

        for index, hour in enumerate(hours):
            score += 1 if hour > 8 else -1
            if score > 0:
                best = index + 1
            else:
                first_seen.setdefault(score, index)
                if score - 1 in first_seen:
                    best = max(best, index - first_seen[score - 1])
        return best
