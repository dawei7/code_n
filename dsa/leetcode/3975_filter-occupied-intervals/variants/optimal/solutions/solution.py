from typing import List


class Solution:
    def filterOccupiedIntervals(
        self,
        occupiedIntervals: List[List[int]],
        freeStart: int,
        freeEnd: int,
    ) -> List[List[int]]:
        merged = []
        for start, end in sorted(occupiedIntervals):
            if not merged or start > merged[-1][1] + 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        answer = []
        for start, end in merged:
            if end < freeStart or start > freeEnd:
                answer.append([start, end])
                continue
            if start < freeStart:
                answer.append([start, freeStart - 1])
            if end > freeEnd:
                answer.append([freeEnd + 1, end])
        return answer
