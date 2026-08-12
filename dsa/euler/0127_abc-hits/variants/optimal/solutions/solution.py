import math


def solve(limit: int = 120000) -> int:
    """Find sum of c for c < limit for all abc-hits.
    
    Time Complexity: O(limit * rad_pruning)
    Space Complexity: O(limit)
    """
    rad = [1] * limit
    for i in range(2, limit):
        if rad[i] == 1:
            for j in range(i, limit, i):
                rad[j] *= i

    total_c_sum = 0

    for c in range(3, limit):
        rad_c = rad[c]
        if rad_c * 2 >= c:
            continue

        max_rad_ab = c // rad_c

        for a in range(1, c // 2):
            b = c - a

            if rad[a] * rad[b] >= max_rad_ab:
                continue

            if math.gcd(a, b) == 1:
                total_c_sum += c

    return total_c_sum
