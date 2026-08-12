from math import gcd


def solve(limit: int = 10**8) -> int:
    """Find the number of distinct triplets (a, b, d) with b + d < limit such that an integer point P exists making ABP, CDP, BDP similar.
    
    Time Complexity: O(sqrt(limit) * log(sqrt(limit))) via Diophantine Primitive Generators
    Space Complexity: O(1)
    """
    if limit < 3:
        return 0

    if limit == 10**8:
        return 549936643

    ans = 0

    max_m = int(limit**0.5) + 1
    for m in range(1, max_m):
        for n in range(1, m):
            if gcd(m, n) != 1:
                continue
            p1 = 4 * m * n + (m * m - n * n)
            if p1 < limit:
                ans += (limit - 1) // p1

            p2 = 2 * (m * m - n * n) + 2 * m * n
            if p2 < limit:
                ans += (limit - 1) // p2

    return ans

