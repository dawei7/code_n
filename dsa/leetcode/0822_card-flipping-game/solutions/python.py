def solve(fronts: list[int], backs: list[int]) -> int:
    blocked = {
        front
        for front, back in zip(fronts, backs)
        if front == back
    }

    smallest: int | None = None
    for front, back in zip(fronts, backs):
        if front not in blocked and (smallest is None or front < smallest):
            smallest = front
        if back not in blocked and (smallest is None or back < smallest):
            smallest = back

    return 0 if smallest is None else smallest
