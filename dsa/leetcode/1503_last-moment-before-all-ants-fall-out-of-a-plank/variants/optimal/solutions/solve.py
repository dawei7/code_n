def solve(n, left, right):
    last_left = max(left, default=0)
    last_right = n - min(right, default=n)
    return max(last_left, last_right)
