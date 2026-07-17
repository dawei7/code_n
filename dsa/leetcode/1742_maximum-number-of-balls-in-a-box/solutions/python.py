def solve(lowLimit: int, highLimit: int) -> int:
    digits = len(str(highLimit))
    counts = [0] * (9 * digits + 1)
    best = 0

    for ball in range(lowLimit, highLimit + 1):
        value = ball
        box = 0
        while value:
            box += value % 10
            value //= 10
        counts[box] += 1
        best = max(best, counts[box])

    return best
