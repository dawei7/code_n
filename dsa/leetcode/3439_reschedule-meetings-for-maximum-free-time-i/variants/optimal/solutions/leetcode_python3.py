from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        gaps = [startTime[0]]
        gaps.extend(startTime[i] - endTime[i - 1] for i in range(1, len(startTime)))
        gaps.append(eventTime - endTime[-1])

        window = sum(gaps[: k + 1])
        best = window
        for right in range(k + 1, len(gaps)):
            window += gaps[right] - gaps[right - k - 1]
            best = max(best, window)
        return best
