from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [startTime[0]]
        gaps.extend(startTime[i] - endTime[i - 1] for i in range(1, n))
        gaps.append(eventTime - endTime[-1])

        prefix = gaps.copy()
        for i in range(1, n + 1):
            prefix[i] = max(prefix[i], prefix[i - 1])

        suffix = gaps.copy()
        for i in range(n - 1, -1, -1):
            suffix[i] = max(suffix[i], suffix[i + 1])

        best = 0
        for i in range(n):
            duration = endTime[i] - startTime[i]
            other_gap = max(prefix[i - 1] if i else 0, suffix[i + 2] if i + 2 <= n else 0)
            merged = gaps[i] + gaps[i + 1]
            if other_gap >= duration:
                merged += duration
            best = max(best, merged)
        return best
