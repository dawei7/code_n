from typing import List


class Solution:
    def maxVacationDays(
        self,
        flights: List[List[int]],
        days: List[List[int]],
    ) -> int:
        city_count = len(flights)
        week_count = len(days[0])
        unreachable = float("-inf")
        totals = [unreachable] * city_count
        totals[0] = 0

        for week in range(week_count):
            next_totals = [unreachable] * city_count

            for origin in range(city_count):
                if totals[origin] == unreachable:
                    continue
                for destination in range(city_count):
                    if (
                        origin == destination
                        or flights[origin][destination]
                    ):
                        next_totals[destination] = max(
                            next_totals[destination],
                            totals[origin] + days[destination][week],
                        )

            totals = next_totals

        return int(max(totals))

