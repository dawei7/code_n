def solve(n, rounds):
    if n <= 0 or not rounds:
        return []
    start = ((rounds[0] - 1) % n) + 1
    end = ((rounds[-1] - 1) % n) + 1
    if start <= end:
        return list(range(start, end + 1))
    return list(range(1, end + 1)) + list(range(start, n + 1))
