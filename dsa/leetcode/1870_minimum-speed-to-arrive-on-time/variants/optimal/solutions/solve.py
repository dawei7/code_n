def solve(dist: list[int], hour: float) -> int:
    if hour <= len(dist) - 1:
        return -1

    def arrives(speed: int) -> bool:
        elapsed = sum((distance + speed - 1) // speed for distance in dist[:-1])
        return elapsed + dist[-1] / speed <= hour

    low, high = 1, 10_000_000
    while low < high:
        middle = (low + high) // 2
        if arrives(middle):
            high = middle
        else:
            low = middle + 1

    return low if arrives(low) else -1
