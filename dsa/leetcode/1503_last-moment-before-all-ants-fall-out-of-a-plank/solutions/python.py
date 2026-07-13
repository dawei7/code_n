def solve(n, left, right):
    best_left = max(left) if left else 0
    best_right = max((n - pos for pos in right), default=0)
    return max(best_left, best_right)
