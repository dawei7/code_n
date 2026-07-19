from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        nonincreasing = [0] * n
        nondecreasing = [0] * n

        for day in range(1, n):
            if security[day - 1] >= security[day]:
                nonincreasing[day] = nonincreasing[day - 1] + 1

        for day in range(n - 2, -1, -1):
            if security[day] <= security[day + 1]:
                nondecreasing[day] = nondecreasing[day + 1] + 1

        return [
            day
            for day in range(time, n - time)
            if nonincreasing[day] >= time and nondecreasing[day] >= time
        ]
