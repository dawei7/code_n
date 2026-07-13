"""Deterministic sparse Fisher-Yates adapter for LeetCode 519."""


def solve(
    rows: int,
    cols: int,
    random_values: list[float],
    operations: list[str],
) -> list[list[int] | None]:
    total = rows * cols
    remaining = total
    remap: dict[int, int] = {}
    results: list[list[int] | None] = []
    draw = 0

    for operation in operations:
        if operation == "reset":
            remaining = total
            remap.clear()
            results.append(None)
            continue
        if operation != "flip":
            raise ValueError(f"Unsupported matrix operation: {operation}")

        uniform = random_values[draw % len(random_values)]
        draw += 1
        ticket = min(int(uniform * remaining), remaining - 1)
        selected = remap.get(ticket, ticket)
        remaining -= 1
        remap[ticket] = remap.get(remaining, remaining)
        remap.pop(remaining, None)
        results.append([selected // cols, selected % cols])

    return results
