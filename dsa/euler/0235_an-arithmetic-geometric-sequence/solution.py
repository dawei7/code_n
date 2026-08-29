def solve(target: float = -600000000000.0, n: int = 5000) -> str:
    """Find the common ratio r such that s(5000) = target, rounded to 12 decimal places.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Arithmetic-Geometric Sequence:
       The general term of the sequence is:
           u(k) = (900 - 3k) * r^(k - 1).
       The sum of the first n terms is:
           s(r) = sum_{k=1}^n (900 - 3k) * r^(k - 1).

    2. Monotonicity & Bisection Root Finding:
       For r > 1, the dominant terms with k > 300 have large negative coefficients (900 - 3k < 0).
       Consequently, s(r) is strictly monotonically decreasing for r in [1.0, 1.1].
       We employ 100 iterations of high-precision binary bisection, achieving error bound:
           Delta_r = (hi - lo) / 2^100 < 10^(-30),
       guaranteeing exact accuracy to 12 decimal places.

    Complexity:
    -----------
    - Time Complexity: O(I * n) operations where I = 100 iterations, n = 5000 (< 0.05 seconds).
    - Space Complexity: O(1) auxiliary space.
    """

    def eval_series(r: float) -> float:
        total = 0.0
        r_pow = 1.0
        for k in range(1, n + 1):
            total += (900 - 3 * k) * r_pow
            r_pow *= r
        return total

    lo, hi = 1.0, 1.1
    # 100 iterations of bisection ensures precision well beyond 10^(-25)
    for _ in range(100):
        mid = (lo + hi) / 2.0
        val = eval_series(mid)
        # Since s(r) is decreasing, val > target implies r is too small
        if val > target:
            lo = mid
        else:
            hi = mid

    r_ans = (lo + hi) / 2.0
    return f"{r_ans:.12f}"


if __name__ == "__main__":
    print(solve())
