from bisect import bisect_right


def solve(
    rects: list[list[int]],
    random_values: list[float],
    draws: int,
) -> list[list[int]]:
    prefix = []
    total = 0
    for x1, y1, x2, y2 in rects:
        total += (x2 - x1 + 1) * (y2 - y1 + 1)
        prefix.append(total)

    position = 0

    def randrange(stop: int) -> int:
        nonlocal position
        uniform = random_values[position % len(random_values)]
        position += 1
        return min(int(uniform * stop), stop - 1)

    def pick() -> list[int]:
        ticket = randrange(total)
        rectangle_index = bisect_right(prefix, ticket)
        previous_total = prefix[rectangle_index - 1] if rectangle_index else 0
        offset = ticket - previous_total
        x1, y1, x2, _ = rects[rectangle_index]
        width = x2 - x1 + 1
        return [x1 + offset % width, y1 + offset // width]

    return [pick() for _ in range(draws)]
