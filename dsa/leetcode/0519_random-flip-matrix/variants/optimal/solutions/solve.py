def solve(
    m: int,
    n: int,
    random_values: list[float],
    operations: list[str],
) -> list[list[int] | None]:
    rows = m
    cols = n
    total = m * n
    remaining = total
    remap = {}
    position = 0

    def randrange(stop: int) -> int:
        nonlocal position
        uniform = random_values[position % len(random_values)]
        position += 1
        return min(int(uniform * stop), stop - 1)

    def flip() -> list[int]:
        nonlocal remaining
        ticket = randrange(remaining)
        selected = remap.get(ticket, ticket)
        remaining -= 1
        remap[ticket] = remap.get(remaining, remaining)
        remap.pop(remaining, None)
        return [selected // cols, selected % cols]

    def reset() -> None:
        nonlocal remaining
        remaining = total
        remap.clear()

    results = []
    for operation in operations:
        if operation == "reset":
            reset()
            results.append(None)
        else:
            results.append(flip())

    return results
