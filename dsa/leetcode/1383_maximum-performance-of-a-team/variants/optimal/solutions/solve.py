from heapq import heappop, heappush


def solve(
    n: int,
    speed: list[int],
    efficiency: list[int],
    k: int,
) -> int:
    engineers = sorted(zip(efficiency, speed), reverse=True)
    speed_heap: list[int] = []
    speed_sum = 0
    best = 0

    for engineer_efficiency, engineer_speed in engineers:
        heappush(speed_heap, engineer_speed)
        speed_sum += engineer_speed
        if len(speed_heap) > k:
            speed_sum -= heappop(speed_heap)
        best = max(best, speed_sum * engineer_efficiency)

    return best % 1_000_000_007
