def solve(arr, k):
    positives = sorted({x for x in arr if x > 0})
    missing = max(1, k)
    current = 1
    for value in positives:
        if value < current:
            continue
        if value == current:
            current += 1
            continue
        gap = value - current
        if missing <= gap:
            return current + missing - 1
        missing -= gap
        current = value + 1
    return current + missing - 1
