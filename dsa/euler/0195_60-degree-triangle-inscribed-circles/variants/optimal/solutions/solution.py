import math


def solve(limit: int = 1053779) -> int:
    """Find T(limit), the number of 60-degree triangles with inradius r <= limit.
    
    Time Complexity: O(limit * log limit)
    Space Complexity: O(1)
    """
    N = limit
    sqrt3 = math.sqrt(3)

    lim_0 = 6 * N / sqrt3

    cnt = 0

    for d in range(1, int(lim_0) + 1):
        max_n = int((2 * N / sqrt3 if d % 3 != 0 else 6 * N / sqrt3) / d)
        for n in range(1, max_n + 1):
            if d == 1 and n == 1:
                continue  # Exclude equilateral
            if math.gcd(n, d) != 1:
                continue

            if (2 * n + d) % 3 != 0:
                r = (sqrt3 / 2) * n * d
            else:
                r = (sqrt3 / 6) * n * d

            if r <= N:
                cnt += int(N / r)

    return cnt // 2
