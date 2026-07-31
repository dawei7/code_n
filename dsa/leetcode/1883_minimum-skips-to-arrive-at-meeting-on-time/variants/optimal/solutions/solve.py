def solve(dist: list[int], speed: int, hoursBefore: int) -> int:
    limit = hoursBefore * speed
    if sum(dist) > limit:
        return -1

    road_count = len(dist)
    infinity = limit + speed * road_count + 1
    best = [infinity] * road_count
    best[0] = 0

    for road_index, distance in enumerate(dist[:-1]):
        next_best = [infinity] * road_count
        for skips in range(road_index + 1):
            elapsed = best[skips] + distance
            rounded = ((elapsed + speed - 1) // speed) * speed
            next_best[skips] = min(next_best[skips], rounded)
            next_best[skips + 1] = min(next_best[skips + 1], elapsed)
        best = next_best

    final_distance = dist[-1]
    for skips in range(road_count):
        if best[skips] + final_distance <= limit:
            return skips
    return -1
