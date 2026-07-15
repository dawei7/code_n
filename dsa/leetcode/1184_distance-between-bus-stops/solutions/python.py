def solve(distance: list[int], start: int, destination: int) -> int:
    if start > destination:
        start, destination = destination, start

    total = 0
    direct = 0
    for index, edge in enumerate(distance):
        total += edge
        if start <= index < destination:
            direct += edge

    return min(direct, total - direct)
