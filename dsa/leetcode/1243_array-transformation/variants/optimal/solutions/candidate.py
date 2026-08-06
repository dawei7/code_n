def solve(arr: list[int]) -> list[int]:
    values = arr[:]
    active = set(range(1, len(values) - 1))

    while active:
        changes: list[tuple[int, int]] = []
        for i in active:
            if values[i] < values[i - 1] and values[i] < values[i + 1]:
                changes.append((i, 1))
            elif values[i] > values[i - 1] and values[i] > values[i + 1]:
                changes.append((i, -1))
        if not changes:
            break

        for i, delta in changes:
            values[i] += delta
        active = {
            j
            for i, _ in changes
            for j in (i - 1, i, i + 1)
            if 0 < j < len(values) - 1
        }

    return values
