def solve(card_points, k):
    n = len(card_points)
    k = max(0, min(int(k), n))
    if k == n:
        return sum(card_points)
    window = n - k
    current = sum(card_points[:window])
    best_middle = current
    for right in range(window, n):
        current += card_points[right] - card_points[right - window]
        best_middle = min(best_middle, current)
    return sum(card_points) - best_middle
