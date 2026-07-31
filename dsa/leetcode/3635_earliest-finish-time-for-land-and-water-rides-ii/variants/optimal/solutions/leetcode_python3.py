from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        earliest_land_finish = min(
            start + duration
            for start, duration in zip(landStartTime, landDuration)
        )
        earliest_water_finish = min(
            start + duration
            for start, duration in zip(waterStartTime, waterDuration)
        )

        land_then_water = min(
            max(earliest_land_finish, start) + duration
            for start, duration in zip(waterStartTime, waterDuration)
        )
        water_then_land = min(
            max(earliest_water_finish, start) + duration
            for start, duration in zip(landStartTime, landDuration)
        )
        return min(land_then_water, water_then_land)
