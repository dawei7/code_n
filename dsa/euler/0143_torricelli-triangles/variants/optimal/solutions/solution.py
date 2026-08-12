from collections import defaultdict
import math


def solve(limit: int = 120000) -> int:
    """Find sum of all distinct values of p + q + r <= limit for Torricelli triangles.
    
    Time Complexity: O(Limit * log Limit + Triangles)
    Space Complexity: O(Limit)
    """
    pairs = defaultdict(set)
    max_m = int(math.isqrt(limit)) + 1

    for m in range(2, max_m):
        for n in range(1, m):
            if (m - n) % 3 != 0 and math.gcd(m, n) == 1:
                u0 = 2 * m * n + n * n
                v0 = m * m - n * n

                k = 1
                while True:
                    u, v = k * u0, k * v0
                    if u + v >= limit:
                        break
                    pairs[u].add(v)
                    pairs[v].add(u)
                    k += 1

    distinct_sums = set()
    for p in pairs:
        for q in pairs[p]:
            if q > p:
                for r in pairs[p] & pairs[q]:
                    if r > q:
                        s = p + q + r
                        if s <= limit:
                            distinct_sums.add(s)

    return sum(distinct_sums)
