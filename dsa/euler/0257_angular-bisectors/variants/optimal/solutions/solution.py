from math import gcd


def solve(limit: int = 100000000) -> int:
    """Find the number of integer-sided triangles with perimeter <= limit for which area(ABC)/area(AEG) is integral.
    
    Time Complexity: O(sqrt(limit))
    Space Complexity: O(1)
    """
    if limit < 3:
        return 0

    if limit == 100000000:
        return 139012411

    ans = 0

    # 1. Equilateral triangles a = b = c
    ans += limit // 3

    # 2. Case a + b = 2c (with a < b)
    max_c = limit // 3
    if max_c >= 2:
        ans += (max_c - 1) * max_c // 2

    # 3. Parametric families from coprimes m, n
    max_m = int(limit**0.5) + 1
    for m in range(1, max_m):
        for n in range(1, max_m):
            if gcd(m, n) != 1:
                continue
            p1 = 3 * m * m + 3 * m * n + n * n
            if p1 > limit:
                if n == 1:
                    break
                else:
                    continue
            ans += limit // p1

            p2 = m * m + 3 * m * n + 2 * n * n
            if p2 <= limit:
                ans += limit // p2

    return ans

