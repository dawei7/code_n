import math


def solve(stations: list[int], k: int) -> float:
    low = 0.0
    high = max(right - left for left, right in zip(stations, stations[1:]))

    for _ in range(70):
        maximum_distance = (low + high) / 2
        required = 0
        for left, right in zip(stations, stations[1:]):
            required += math.ceil((right - left) / maximum_distance) - 1
            if required > k:
                break
        if required <= k:
            high = maximum_distance
        else:
            low = maximum_distance
    return high
