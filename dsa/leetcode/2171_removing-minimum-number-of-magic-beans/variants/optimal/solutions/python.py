def solve(beans: list[int]) -> int:
    ordered = sorted(beans)
    total = sum(ordered)
    maximum_kept = 0

    for index, amount in enumerate(ordered):
        maximum_kept = max(
            maximum_kept,
            amount * (len(ordered) - index),
        )

    return total - maximum_kept
