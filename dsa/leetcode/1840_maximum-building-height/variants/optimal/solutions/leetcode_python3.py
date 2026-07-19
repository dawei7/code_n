from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        limits = [[1, 0], *restrictions, [n, n - 1]]
        limits.sort()

        for index in range(1, len(limits)):
            distance = limits[index][0] - limits[index - 1][0]
            limits[index][1] = min(
                limits[index][1], limits[index - 1][1] + distance
            )

        for index in range(len(limits) - 2, -1, -1):
            distance = limits[index + 1][0] - limits[index][0]
            limits[index][1] = min(
                limits[index][1], limits[index + 1][1] + distance
            )

        answer = 0
        for index in range(1, len(limits)):
            distance = limits[index][0] - limits[index - 1][0]
            peak = (
                limits[index - 1][1] + limits[index][1] + distance
            ) // 2
            answer = max(answer, peak)

        return answer
