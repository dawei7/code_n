def solve(buckets: list[int], loss: int) -> float:
    left = float(min(buckets))
    right = float(max(buckets))
    retained = 1.0 - loss / 100.0

    for _ in range(60):
        middle = (left + right) / 2.0
        surplus = 0.0
        deficit = 0.0
        for amount in buckets:
            if amount > middle:
                surplus += amount - middle
            else:
                deficit += middle - amount
        if surplus * retained >= deficit:
            left = middle
        else:
            right = middle
    return left
