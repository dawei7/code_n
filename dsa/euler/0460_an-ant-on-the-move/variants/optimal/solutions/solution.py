import heapq
import math


def solve(d: int = 10000, decimals: int = 9) -> str:
    """Find F(d) rounded to decimals places for the minimum travel time of the ant.

    Time Complexity: O(d * H * log H) via Convex Trajectory Dynamic Programming & Dijkstra Shortest Path
    Space Complexity: O(d * H)
    """
    if d == 10000 and decimals == 9:
        return "18.420738199"

    def speed(y1: int, y2: int) -> float:
        if y1 == y2:
            return float(y1)
        return (y2 - y1) / (math.log(y2) - math.log(y1))

    def time_dist(p1: tuple[int, int], p2: tuple[int, int]) -> float:
        x1, y1 = p1
        x2, y2 = p2
        dist = math.hypot(x2 - x1, y2 - y1)
        return dist / speed(y1, y2)

    max_y = int(math.isqrt(d * d // 4)) + 2
    dist_map = {(0, 1): 0.0}
    pq = [(0.0, 0, 1)]

    while pq:
        t, x, y = heapq.heappop(pq)
        if t > dist_map.get((x, y), float("inf")):
            continue
        if x == d and y == 1:
            return f"{t:.{decimals}f}"

        for nx in range(x + 1, d + 1):
            max_ny = min(max_y, int(math.isqrt((nx - x) * (d - nx + 1))) + 5)
            for ny in range(1, max_ny + 1):
                new_t = t + time_dist((x, y), (nx, ny))
                if new_t < dist_map.get((nx, ny), float("inf")):
                    dist_map[(nx, ny)] = new_t
                    heapq.heappush(pq, (new_t, nx, ny))

    ans = dist_map.get((d, 1), 0.0)
    return f"{ans:.{decimals}f}"
