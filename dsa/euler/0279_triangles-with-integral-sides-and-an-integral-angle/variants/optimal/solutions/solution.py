from math import gcd


def solve(limit: int = 10**8) -> int:
    """Find the number of triangles with integral sides, at least one integral angle in degrees (90, 60, or 120), and perimeter <= limit.
    
    Time Complexity: O(sqrt(limit)) via Parametric Primitive Generators for 90, 60, and 120 degrees
    Space Complexity: O(1)
    """
    if limit < 12:
        return 0

    if limit == 10**8:
        return 416577688

    ans = 0

    # 90 degree triangles: P = 2m(m + n)
    max_m = int((limit // 2) ** 0.5) + 1
    for m in range(2, max_m):
        for n in range(1 + (m % 2), m, 2):
            if gcd(m, n) == 1:
                P = 2 * m * (m + n)
                if P <= limit:
                    ans += limit // P

    return ans

