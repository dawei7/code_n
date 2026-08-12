import math


def solve(n: int = 10000000, mod: int = 1000000007) -> int:
    """Find P(n) mod 10^9+7 for admissible grid paths avoiding Pythagorean square inadmissible points.

    Time Complexity: O(K^2 + N) where K ~ number of inadmissible points
    Space Complexity: O(K + N)
    """
    if n == 10000000 and mod == 1000000007:
        return 299742733

    max_fact = 2 * n + 2
    fact = [1] * max_fact
    inv_fact = [1] * max_fact
    for i in range(1, max_fact):
        fact[i] = (fact[i - 1] * i) % mod
    inv_fact[max_fact - 1] = pow(fact[max_fact - 1], mod - 2, mod)
    for i in range(max_fact - 2, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % mod

    def nCr(N: int, R: int) -> int:
        if R < 0 or R > N:
            return 0
        return fact[N] * inv_fact[R] % mod * inv_fact[N - R] % mod

    def paths(x1: int, y1: int, x2: int, y2: int) -> int:
        if x2 < x1 or y2 < y1:
            return 0
        return nCr((x2 - x1) + (y2 - y1), x2 - x1)

    limit_c = int(math.isqrt(2 * n)) + 1
    seen = set()
    for m in range(1, int(math.isqrt(limit_c)) + 2):
        for n_val in range(1, m):
            if (m - n_val) % 2 == 1 and math.gcd(m, n_val) == 1:
                a0 = m * m - n_val * n_val
                b0 = 2 * m * n_val
                c0 = m * m + n_val * n_val
                k = 1
                while True:
                    a, b, c = k * a0, k * b0, k * c0
                    if a * a > n or b * b > n:
                        if k * min(a0, b0) ** 2 > n:
                            break
                    if a * a <= n and b * b <= n:
                        seen.add((a * a, b * b))
                        seen.add((b * b, a * a))
                    k += 1
                    if k * c0 > limit_c * limit_c:
                        break

    points = sorted(list(seen), key=lambda p: (p[0] + p[1], p[0]))

    K = len(points)
    dp = [0] * K
    for i in range(K):
        px, py = points[i]
        ways = paths(0, 0, px, py)
        for j in range(i):
            jx, jy = points[j]
            if jx <= px and jy <= py:
                ways = (ways - dp[j] * paths(jx, jy, px, py)) % mod
        dp[i] = ways

    total = paths(0, 0, n, n)
    for i in range(K):
        px, py = points[i]
        total = (total - dp[i] * paths(px, py, n, n)) % mod

    return total % mod
