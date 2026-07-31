from typing import List


class Solution:
    def minimumFinishTime(
        self, tires: List[List[int]], changeTime: int, numLaps: int
    ) -> int:
        infinity = 10**30
        fastest_fresh_lap = min(first for first, _ in tires)
        best_stint = [infinity] * (numLaps + 1)
        longest_stint = 0

        for first, ratio in tires:
            stint_total = 0
            lap_time = first
            stint_length = 1

            while (
                stint_length <= numLaps
                and lap_time <= changeTime + fastest_fresh_lap
            ):
                stint_total += lap_time
                best_stint[stint_length] = min(
                    best_stint[stint_length], stint_total
                )
                longest_stint = max(longest_stint, stint_length)
                lap_time *= ratio
                stint_length += 1

        best_total = [infinity] * (numLaps + 1)
        best_total[0] = -changeTime

        for laps in range(1, numLaps + 1):
            for stint_length in range(1, min(laps, longest_stint) + 1):
                best_total[laps] = min(
                    best_total[laps],
                    best_total[laps - stint_length]
                    + changeTime
                    + best_stint[stint_length],
                )

        return best_total[numLaps]
