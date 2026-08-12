def solve(target: float = -600000000000.0, n: int = 5000) -> str:
    """Find r such that sum_{k=1..n} (900 - 3k) r^(k-1) = target, rounded to 12 decimal places.
    
    Time Complexity: O(n * log(1 / eps)) via Bisection Search
    Space Complexity: O(1)
    """

    def s(r):
        total = 0.0
        r_pow = 1.0
        for k in range(1, n + 1):
            total += (900 - 3 * k) * r_pow
            r_pow *= r
        return total

    lo, hi = 1.0, 1.1
    for _ in range(100):
        mid = (lo + hi) / 2.0
        val = s(mid)
        if val > target:
            lo = mid
        else:
            hi = mid

    r_ans = (lo + hi) / 2.0
    return f"{r_ans:.12f}"
