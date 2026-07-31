def solve(road: str, budget: int) -> int:
    runs = sorted(
        (len(block) for block in road.split(".") if block),
        reverse=True,
    )

    repaired = 0
    for length in runs:
        if budget <= 1:
            break
        fixed = min(length, budget - 1)
        repaired += fixed
        budget -= fixed + 1

    return repaired
