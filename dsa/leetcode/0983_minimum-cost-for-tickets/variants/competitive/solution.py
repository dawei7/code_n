from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (len(days) + 1)
        week = 0
        month = 0

        for i, day in enumerate(days):
            while days[week] < day - 6:
                week += 1
            while days[month] < day - 29:
                month += 1
            dp[i + 1] = min(
                dp[i] + costs[0],
                dp[week] + costs[1],
                dp[month] + costs[2],
            )

        return dp[-1]
