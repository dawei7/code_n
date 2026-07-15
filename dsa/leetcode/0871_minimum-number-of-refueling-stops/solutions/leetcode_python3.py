import heapq
from typing import List


class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        reachable = startFuel
        station_index = 0
        stops = 0
        available_fuel = []

        while reachable < target:
            while (
                station_index < len(stations)
                and stations[station_index][0] <= reachable
            ):
                heapq.heappush(available_fuel, -stations[station_index][1])
                station_index += 1

            if not available_fuel:
                return -1

            reachable += -heapq.heappop(available_fuel)
            stops += 1

        return stops
