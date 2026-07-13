def solve(n, ranges):
    farthest = [0] * (n + 1)
    for i, radius in enumerate(ranges):
        left = max(0, i - radius)
        right = min(n, i + radius)
        farthest[left] = max(farthest[left], right)

    taps = 0
    current_end = 0
    next_end = 0
    for i in range(n):
        next_end = max(next_end, farthest[i])
        if i == current_end:
            if next_end <= i:
                return -1
            taps += 1
            current_end = next_end
    return taps
