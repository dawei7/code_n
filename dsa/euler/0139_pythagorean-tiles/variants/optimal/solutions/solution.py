import math


def solve(limit: int = 100000000) -> int:
    """Find number of Pythagorean triangles with perimeter < limit that allow central hole tiling.
    
    Time Complexity: O(sqrt(limit))
    Space Complexity: O(1)
    """
    total_count = 0
    max_m = int((limit // 2)**0.5)

    for m in range(2, max_m + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n

                perim = a + b + c
                if perim >= limit:
                    break

                hole = abs(b - a)
                if c % hole == 0:
                    total_count += (limit - 1) // perim

    return total_count
